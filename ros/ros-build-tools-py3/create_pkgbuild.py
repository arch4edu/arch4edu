#! /usr/bin/env python3

from __future__ import print_function

import catkin_pkg.package
from argparse import ArgumentParser
import sys
import os
import os.path
import urllib3
import yaml
import re
from collections import OrderedDict
from termcolor import colored, cprint
import pickle
import subprocess
import hashlib
import shutil

# Directory containing some data files
updates_packages_dir = "/tmp/create_pkgbuild"

# File that contains the dump file of updated packages
updated_packages_filename = os.path.join(updates_packages_dir,
                                         "updated_packages_%(distro)s.dump")

# File that contains the list of packages to install
makepkg_filename = os.path.join(updates_packages_dir,
                                "makepkg_%(distro)s.dump")

http = urllib3.PoolManager()

try:
    import certifi

    # Make verified HTTPS requests
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',  # Force certificate check.
        ca_certs=certifi.where(),  # Path to the Certifi bundle.
    )
except ImportError as e:
    # HTTPS requests will not be verified
    pass


class PackageBase(object):

    def __init__(self, distro, repository_url, name, version):
        self.packages = []
        self.distro = distro
        self.repository_url = repository_url
        self.repository_name = self.repository_url.split('/')[-1].split('.')[0]
        package = self._parse_package_file(
            self._get_package_xml_url(repository_url, name, version))
        self.name = package.name
        self.version = package.version
        # TODO:  PKG_RRELEASE_VAR: How could we handle this?
        # self.package_release = str(int(version_patch) + 1)
        self.package_release = str(1)
        self.licenses = package.licenses
        self.run_dependencies = list(OrderedDict.fromkeys([dependency.name for dependency in package.run_depends]))
        self.build_dependencies = list(
            OrderedDict.fromkeys([dependency.name for dependency in package.build_depends + package.buildtool_depends]))

        # Tarball
        self.tarball_url = "%s/archive/release/%s/%s/%s.tar.gz" \
                           % (self.repository_url.replace('.git', ''),
                              self.distro.name, self.name,
                              self.version)
        self.tarball_dir = "%s-release-%s-%s-%s" \
                           % (self.repository_name, self.distro.name, self.name,
                              self.version)

        # This may be the case for some metapackages
        self.is_virtual = False

        # Build dependencies already added:
        if 'git' in self.build_dependencies:
            self.build_dependencies.remove('git')
        if 'cmake' in self.build_dependencies:
            self.build_dependencies.remove('cmake')

        # Remove HTML tags from description
        self.description = re.sub('<[^<]+?>', '', package.description)
        # Put it on one line to motivate packagers to make shorter descriptions
        self.description = re.sub('\n', ' ', self.description)
        # Convert tabs to spaces
        self.description = re.sub('\t', ' ', self.description)
        # Multiple consecutive spaces turned into one
        self.description = re.sub('([ ]+)', ' ', self.description)
        # Only take the first sentence (keep short description)
        self.description = re.split("\. |\.$", self.description)[0] + "."
        # Handle quotes
        self.description = self.description.replace('"', '').replace('`', '').replace('&quot;', '').replace('\'', '')

        # Website URL
        self.site_url = "http://www.ros.org/"
        for url in package.urls:
            if url.type == "website":
                # Some maintainers provide wrong URLs...
                url.url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]'
                                     '|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url.url)
            if url.url:
                self.site_url = url.url[0]

    def _parse_package_file(self, url):
        """
    Parses the package.xml file specified by `url`.

    Arguments:
    - `url`: Valid URL pointing to a package.xml file.
    """
        return catkin_pkg.package.parse_package_string(http.request('GET', url).data)

    def _fix_dependencies(self, rosdep_urls, build_dep, run_dep):
        # Fix usual non-ROS dependencies:
        #  - load replacement dictionary: these are found in rosdep yaml files. We
        #                                 just need to download and merge these files
        #                                 in a dictionary.
        dependency_map = self._get_rosdep_dictionary(rosdep_urls)

        def _fix_dependencies_with_map(dependencies):
            fixed_dependencies = set()
            #  - replace in other_dependencies
            for index, dep in enumerate(dependencies):
                if (dep in dependency_map):
                    # The map may replace one package by multiple ones, or even by none
                    for package in dependency_map[dep]:
                        fixed_dependencies.add(package)
                else:
                    fixed_dependencies.add(dep)
            # Fix some possibly missing Python 2/3 package conflicts
            if self.distro.python_major() == "2":
                fixed_dependencies = [self._ensure_python2_dependency(dependency)
                                      for dependency in fixed_dependencies]
            elif self.distro.python_major() == "3":
                fixed_dependencies = [self._ensure_python3_dependency(dependency)
                                      for dependency in fixed_dependencies]
                return fixed_dependencies

        fixed_build_dep = _fix_dependencies_with_map(build_dep)
        fixed_run_dep = _fix_dependencies_with_map(run_dep)

        return fixed_build_dep, fixed_run_dep

    def _get_ros_dependencies(self):
        """
    Returns (build_dependencies, run_dependencies)
    """
        known_packages = self.distro.package_names(expand_metapackages=True)
        build_dep = list(set([self._get_full_package_name(dependency)
                              for dependency in self.build_dependencies if dependency in known_packages]))
        run_dep = list(set([self._get_full_package_name(dependency)
                            for dependency in self.run_dependencies if dependency in known_packages]))
        return build_dep, run_dep

    def _get_non_ros_dependencies(self, rosdep_urls=[]):
        """
        Returns (build_dependencies, run_dependencies)
        """
        known_packages = self.distro.package_names(expand_metapackages=True)

        other_build_dep = list(set([dependency for dependency in self.build_dependencies
                                    if dependency not in known_packages]))
        other_run_dep = list(set([dependency for dependency in self.run_dependencies
                                  if dependency not in known_packages]))
        return self._fix_dependencies(rosdep_urls, other_build_dep, other_run_dep)

    def _rosify_package_name(self, name):
        return name.replace('_', '-')

    def _get_full_package_name(self, name):
        return "ros-%s-%s" % (self.distro.name, name.replace('_', '-'))

    def _ensure_python2_dependency(self, dependency):
        # python     ---> python2
        # python-foo ---> python2-foo
        return re.sub(r'^python(?!2)([a-zA-Z0-9\-]*)', r'python2\1', dependency)

    def _ensure_python3_dependency(self, dependency):
        # python2     ---> python
        # python2-foo ---> python-foo
        return re.sub(r'^python2([a-zA-Z0-9\-]*)', r'python\1', dependency)

    def _get_package_xml_url(self, url, name, version):
        if url.find('github'):
            return github_raw_url(url, 'package.xml', 'release/%s/%s' % (self.distro.name, name))
        else:
            raise Exception('Unable to generate url for package.xml')

    def _get_rosdep_dictionary(self, rosdep_urls):
        dependency_map = {}
        for rosdep_url in rosdep_urls:
            stream = http.request('GET', rosdep_url).data
            rosdep_file = yaml.load(stream, Loader=yaml.BaseLoader)
            for package_name, distrib in rosdep_file.items():
                if 'arch' in distrib:
                    if 'pacman' in distrib["arch"]:
                        dependency_map[package_name] = distrib["arch"]["pacman"]["packages"]
                    elif 'aur' in distrib["arch"]:
                        dependency_map[package_name] = distrib["arch"]["aur"]
                    else:
                        dependency_map[package_name] = distrib["arch"]
        return dependency_map

    def _download_tarball(self, url, path, name):
        """
    Download the tarball of the package, and prepend the package name to avoid
    clashes.
    """
        tarball_path = "%s/%s-%s" % (path, name, url.split('/')[-1])
        if not os.path.exists(tarball_path):
            with http.request('GET', url, preload_content=False) \
                    as r, open(tarball_path, 'wb') as out_file:
                shutil.copyfileobj(r, out_file)
        return hashlib.sha256(open(tarball_path, 'rb').read()).hexdigest()

    def generate(self, exclude_dependencies=[], rosdep_urls=[], output_dir=None):
        raise Exception('`generate` not implemented.')

    def is_same_version(self, pkgbuild_file):
        """
        Checks whether a currently installed PKGBUILD contains the same version.
        """
        if os.path.isfile(pkgbuild_file):
            f = open(pkgbuild_file, "r")
            content = f.read()
            pattern_pkgver = re.compile(r"pkgver='([0-9\.]*)'")
            match_pkgver = re.search(pattern_pkgver, content)
            if match_pkgver:
                return (match_pkgver.group(1) == self.version)
            else:
                return False
        else:
            return False


class Package(PackageBase):
    BUILD_TEMPLATE = """# Script generated with create_pkgbuild.py
    # For more information: https://github.com/ros-melodic-arch/ros-build-tools-py3
    pkgdesc="ROS - %(description)s"
    url='%(site_url)s'

    pkgname='ros-%(distro)s-%(arch_package_name)s'
    pkgver='%(package_version)s'
    arch=('any')
    pkgrel=%(package_release)s
    license=('%(license)s')

    ros_makedepends=(%(ros_build_dependencies)s)
    makedepends=('cmake' 'ros-build-tools'
    ${ros_makedepends[@]}
    %(other_build_dependencies)s)

    ros_depends=(%(ros_run_dependencies)s)
    depends=(${ros_depends[@]}
    %(other_run_dependencies)s)

    build() {
        # Use ROS environment variables
        source /usr/share/ros-build-tools/clear-ros-env.sh
        [ -f /opt/ros/%(distro)s/setup.bash ] && source /opt/ros/%(distro)s/setup.bash

        # Create build directory
        [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
        cd ${srcdir}/build

        # Fix Python2/Python3 conflicts
        /usr/share/ros-build-tools/fix-python-scripts.sh -v %(python_version_major)s ${srcdir}/${_dir}

        # Build project
        cmake ${srcdir}/${_dir} \\
                -DCMAKE_BUILD_TYPE=Release \\
                -DCATKIN_BUILD_BINARY_PACKAGE=%(binary)s \\
                -DCMAKE_INSTALL_PREFIX=/opt/ros/%(distro)s \\
                -DPYTHON_EXECUTABLE=%(python_executable)s \\
                -DPYTHON_INCLUDE_DIR=%(python_include_dir)s \\
                -DPYTHON_LIBRARY=%(python_library)s \\
                -DPYTHON_BASENAME=%(python_basename)s \\
                -DSETUPTOOLS_DEB_LAYOUT=OFF
    make
    }

    package() {
    cd "${srcdir}/build"
    make DESTDIR="${pkgdir}/" install
    }
    """

    def generate(self, python_version, exclude_dependencies=[], rosdep_urls=[],
                 output_dir=None):
        raw_build_dep, raw_run_dep = self._get_ros_dependencies()
        ros_build_dep = [dependency for dependency in raw_build_dep
                         if dependency not in exclude_dependencies]
        ros_run_dep = [dependency for dependency in raw_run_dep
                       if dependency not in exclude_dependencies]

        #TODO: Is the outprint necessary ?
        #print(rosdep_urls)
        other_raw_build_dep, other_raw_run_dep = self._get_non_ros_dependencies(rosdep_urls)
        other_build_dep = [dependency for dependency in other_raw_build_dep
                           if dependency not in exclude_dependencies]
        other_run_dep = [dependency for dependency in other_raw_run_dep
                         if dependency not in exclude_dependencies]

        python_version_major = python_version.split('.')[0]
        python_version_full = python_version
        # Python 3 include directory is /usr/include/python3.4m... Because why not?
        if python_version_major == "3":
            python_version_full = "%s%s" % (python_version_full, "m")

        # PYTHON_BASENAME for PySide:
        # If Python 2.7: PySideConfig{-python2.7}.cmake
        python_basename = "-python2.7"
        if python_version_major == "3":
            # If Python 3.4: PySideConfig{.cpython-34m}.cmake
            python_basename = ".cpython-%s" % (python_version_full.replace(".", ""))

        pkgbuild = self.BUILD_TEMPLATE % {
            'distro': self.distro.name,
            'arch_package_name': self._rosify_package_name(self.name),
            'package_name': self.name,
            'package_version': self.version,
            'package_release': self.package_release,
            'package_url': self.repository_url,
            'license': ', '.join(self.licenses),
            'description': self.description,
            'site_url': self.site_url,
            'tarball_url': "%s/archive/release/%s/%s/${pkgver}.tar.gz"
                           % (self.repository_url.replace('.git', ''),
                              self.distro.name, self.name),
            'tarball_dir': "%s-release-%s-%s-${pkgver}"
                           % (self.repository_name, self.distro.name, self.name),
            'tarball_sha': self._download_tarball(self.tarball_url, output_dir,
                                                  "ros-%s-%s" % (self.distro.name,
                                                                 self._rosify_package_name(self.name))),
            'ros_build_dependencies': '\n  '.join(ros_build_dep),
            'ros_run_dependencies': '\n  '.join(ros_run_dep),
            'other_build_dependencies': '\n  '.join(other_build_dep),
            'other_run_dependencies': '\n  '.join(other_run_dep),
            'binary': "OFF" if self.name == "catkin" else "ON",
            'python_version_major': python_version_major,
            'python_executable': '/usr/bin/python%s' % python_version_major,
            'python_include_dir': '/usr/include/python%s' % python_version_full,
            'python_library': '/usr/lib/libpython%s.so' % python_version_full,
            'python_basename': python_basename
        }

        # Post-processing:
        # Remove useless carriage return
        pkgbuild = re.sub('\\n  \)', ')', pkgbuild)
        return pkgbuild


class MetaPackage(PackageBase):
    BUILD_TEMPLATE = """# Script generated with create_pkgbuild.py
  # For more information: https://github.com/ros-melodic-arch/ros-build-tools-py3
  pkgdesc="ROS - %(description)s"
  url='%(site_url)s'

  pkgname='ros-%(distro)s-%(arch_package_name)s'
  pkgver='%(package_version)s'
  arch=('any')
  pkgrel=%(package_release)s
  license=('%(license)s')

  ros_makedepends=(%(ros_build_dependencies)s)
  makedepends=('cmake' 'ros-build-tools'
  ${ros_makedepends[@]}
  %(other_build_dependencies)s)

  ros_depends=(%(ros_run_dependencies)s)
  depends=(${ros_depends[@]}
  %(other_run_dependencies)s)
 
  source=()
  md5sums=()
  """

    def __init__(self, distro, repository_url, name, version):
        try:
            super(MetaPackage, self).__init__(distro, repository_url, name, version)
        except urllib3.exceptions.HTTPError:
            # Virtual metapackage
            # TODO: there should be a cleaner way to deal with this...
            self.name = name
            self.is_virtual = True
        self.packages = [Package(distro, repository_url, child_name, version)
                         for child_name in distro.meta_package_package_names(name)]

    def generate(self, exclude_dependencies=[], rosdep_urls=[]):
        raw_build_dep, raw_run_dep = self._get_ros_dependencies()
        ros_build_dep = [dependency for dependency in raw_build_dep
                         if dependency not in exclude_dependencies]
        ros_run_dep = [dependency for dependency in raw_run_dep
                       if dependency not in exclude_dependencies]

        other_raw_build_dep, other_raw_run_dep = self._get_non_ros_dependencies(rosdep_urls)
        other_build_dep = [dependency for dependency in other_raw_build_dep
                           if dependency not in exclude_dependencies]
        other_run_dep = [dependency for dependency in other_raw_run_dep
                         if dependency not in exclude_dependencies]
        pkgbuild = self.BUILD_TEMPLATE % {
            'distro': self.distro.name,
            'arch_package_name': self._rosify_package_name(self.name),
            'package_name': self.name,
            'package_version': self.version,
            'package_release': self.package_release,
            'license^': ', '.join(self.licenses),
            'description': self.description,
            'site_url': self.site_url,
            'ros_build_dependencies': '\n  '.join(ros_build_dep),
            'ros_run_dependencies': '\n  '.join(ros_run_dep),
            'other_build_dependencies': '\n  '.join(other_build_dep),
            'other_run_dependencies': '\n  '.join(other_run_dep)
        }

        # Post-processing:
        # Remove useless carriage return
        pkgbuild = re.sub('\${ros_depends\[@\]}\\n  \)',
                          '${ros_depends[@]})', pkgbuild)
        return pkgbuild


class DistroDescription(object):

    def __init__(self, name, url, python_version):
        stream = http.request('GET', url).data
        self.name = name
        self._distro = yaml.load(stream, Loader=yaml.BaseLoader)
        self._package_cache = {}
        self.python_version = python_version
        if 'metapackages' in self._distro['repositories'].keys():
            metapackages = self._distro['repositories']['metapackages']['release']
            for meta in metapackages['packages']:
                self._distro['repositories'][meta] = {}
                self._distro['repositories'][meta]['release'] = {}
                self._distro['repositories'][meta]['release']['url'] = metapackages['url']
                self._distro['repositories'][meta]['release']['version'] = metapackages['version']
            del self._distro['repositories']['metapackages']

    def package_names(self, expand_metapackages=False):
        packages = [name for name in self._distro['repositories'].keys()]
        if expand_metapackages:
            return sum([([name] + self.meta_package_package_names(name)) if self._is_meta_package(name) else [name]
                        for name in packages],
                       [])
        else:
            return packages

    def is_package(self, name):
        return self._get_package_data(name) is not None

    def package(self, name):
        package_data = self._get_package_data(name)
        if not package_data:
            raise Exception('Unable to find package `%s`' % name)
        if self._package_cache.get(name):
            return self._package_cache[name]
        url = package_data['url']
        version = package_data['version'].split('-')[0]
        # WARNING: some metapackages embed a package with the same name. In this case,
        #          we treat the package as a normal package.
        if self._is_meta_package(name) and (not name in self._distro['repositories'][name]['release']['packages']):
            package = MetaPackage(self, url, name, version)
        else:
            package = Package(self, url, name, version)
        self._package_cache[name] = package
        return package

    def meta_package_package_names(self, name):
        return self._distro['repositories'][name]['release']['packages']

    def python_major(self):
        """
    Return the major version number of Python.
    """
        return self.python_version.split('.')[0]

    def _is_meta_package(self, name):
        if self._distro['repositories'].get(name) != None:
            if self._distro['repositories'][name].get('release') != None:
                return (self._distro['repositories'][name]['release'].get('packages') != None)

    def _get_package_data(self, name):
        """
    Searches for `name` in all known packages and metapackages.
    """
        if self._distro['repositories'].get(name):
            try:
                return self._distro['repositories'][name]['release']
            except KeyError as e:
                print(colored("Missing %s branch for %s" % (e, name),
                              'red', attrs=['bold']))
        else:
            for package in self.package_names():
                if (self._is_meta_package(package)
                        and name in self._distro['repositories'][package]['release']['packages']):
                    return self._distro['repositories'][package]['release']


def list_packages(distro_desc, distro_dir=None):
    """
    List available packages.
    """
    if not distro_dir or not os.path.isdir(distro_dir):
        print(*sorted(distro_desc.package_names()), sep='\n')
    else:
        # For each package, check if a PKGBUILD has already been generated
        for name in sorted(distro_desc.package_names()):
            if os.path.isfile(os.path.join(distro_dir, name, "PKGBUILD")):
                print("[✓] %s" % (colored(name, 'green', attrs=['bold'])))
            else:
                print("[ ] %s" % name)


# From http://code.activestate.com/recipes/577058/ (r2)
def query_yes_no(question, default="yes"):
    """
    Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes": "yes", "y": "yes", "ye": "yes",
             "no": "no", "n": "no"}
    if not default:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        print(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').")


def github_raw_url(repo_url, path, commitish):
    """
    Returns the URL of the file blob corresponding to `path` in the
    github repository `repo_url` in branch, commit or tag `commitish`.
    """
    url = urllib3.util.parse_url(repo_url)
    return 'https://raw.%(host)s%(repo_path)s/%(branch)s/%(path)s' % {
        'host': url.host,
        'repo_path': url.path.replace('.git', ''),
        'branch': commitish,
        'path': path
    }


def create_clone(url_ro, url_rw, full_dir):
    subprocess.check_call(['git', 'clone', url_ro, full_dir],
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    subprocess.check_call(['git', '-C', full_dir, 'remote', 'set-url', '--push',
                           'origin', url_rw], stderr=subprocess.PIPE,
                          stdout=subprocess.PIPE)


def create_package_directory(directory, package):
    """
    Create a directory or an AUR git repo based on the context.
    """
    full_dir = os.path.join(directory, package.name)

    full_package_name = package._get_full_package_name(package.name)
    url_ro = "https://aur.archlinux.org/%s.git" % (full_package_name)
    url_rw = "ssh+git://aur@aur.archlinux.org/%s.git" % (full_package_name)

    if not os.path.exists(full_dir):
        print("Creating new dir")
        try:
            create_clone(url_ro, url_rw, full_dir)
        except subprocess.CalledProcessError:
            os.mkdir(full_dir, 644)

    return full_dir


def generate_pkgbuild(distro, package, directory, force=False,
                      no_overwrite=False, recursive=False, update=False,
                      exclude_dependencies=[], rosdep_urls=[],
                      generated=None, written=None):
    """
    Generate a PKGBUILD file for the given package and the given ROS
    distribution.
    """
    if generated is None:
        generated = set()
    elif package.name in generated:
        return

    generated.add(package.name)

    if distro._is_meta_package(package.name):
        for child_name in distro.meta_package_package_names(package.name):
            generate_pkgbuild(distro, distro.package(child_name), directory,
                              force=force,
                              exclude_dependencies=exclude_dependencies,
                              no_overwrite=no_overwrite, recursive=recursive,
                              update=update, rosdep_urls=rosdep_urls,
                              generated=generated, written=written)

    # If this is a virtual package (i.e. not an actual package)
    if package.is_virtual:
        return

    if recursive:
        for dependency in package.run_dependencies + package.build_dependencies:
            if distro.is_package(dependency):
                generate_pkgbuild(distro, distro.package(dependency), directory,
                                  force=force, no_overwrite=no_overwrite, recursive=recursive,
                                  exclude_dependencies=exclude_dependencies, update=update,
                                  rosdep_urls=rosdep_urls, generated=generated,
                                  written=written)

    # If the directory/repo/package does not exist, create it
    output_directory = create_package_directory(directory, package)

    pkgbuild_file = os.path.join(output_directory, 'PKGBUILD')

    # If we are merely updating packages
    if update:
        if package.is_same_version(pkgbuild_file):
            print('PKGBUILD for package %s already up-to-date (%s)'
                  % (colored(package.name, 'yellow', attrs=['bold']),
                     colored(package.version, 'white',
                             attrs=['bold'])))
        return

    # If PKGBUILD already exists
    if os.path.exists(os.path.join(output_directory, 'PKGBUILD')):
        if no_overwrite:
            return
        elif not force and query_yes_no(
                "Directory '%s' already contains a PKGBUILD file. Overwrite?" % (
                        output_directory)) == "no":
            return

    print('Generating PKGBUILD for package %s (%s)'
          % (colored(package.name, 'green', attrs=['bold']),
             colored(package.version, 'white',
                     attrs=['bold'])))

    # Write PKGBUILD file
    with open(pkgbuild_file, 'w') as pkgbuild:
        pkgbuild.write(package.generate(distro.python_version, exclude_dependencies,
                                        rosdep_urls, output_directory))

    # Add the package to the txt file containing packages to install
    if written:
        written["packages"].append(package.name)


def main():
    parser = ArgumentParser(prog='create_pkgbuild', add_help=True)
    parser.add_argument('package', type=str, nargs='+')
    parser.add_argument('--distro', default='melodic', metavar='distro',
                        help='Select the ROS distro to use.')
    parser.add_argument('--list-packages', dest='list_packages', action='store_true',
                        default=False, help='Lists all available packages.')
    parser.add_argument('--output-directory', metavar='output_directory',
                        default=None,
                        help='The output directory. Packages are put into '
                             '<output-directory>/<name>')
    default_distro_url = 'https://raw.github.com/ros/rosdistro/master/%s/distribution.yaml'
    parser.add_argument('--distro-url', metavar='distro_url',
                        default=default_distro_url,
                        help='The URL of the distro description. %s is replaced by '
                             'the actual distro name')
    default_rosdep_url = 'https://raw.github.com/ros/rosdistro/master/rosdep/%s.yaml'
    parser.add_argument('--rosdep-urls', metavar='rosdep_urls',
                        default=[default_rosdep_url % 'base',
                                 default_rosdep_url % 'python',
                                 default_rosdep_url % 'ruby'],
                        help='The URLs of the rosdep mapping files.')
    parser.add_argument('--exclude-dependencies', metavar='exclude_dependencies',
                        default='',
                        help='Comma-separated list of (source) package dependencies \
                              to exclude from the generated PKGBUILD file.')
    parser.add_argument('--python-version', metavar='python_version', default='',
                        help='Python version that will be used. Accepted values are 2.7 or 3')
    parser.add_argument('-f', '--force', dest='force', action='store_true',
                        default=False,
                        help='Always overwrite existing PKGBUILD files.')
    parser.add_argument('-n', '--no-overwrite', dest='no_overwrite',
                        action='store_true', default=False,
                        help='Do not overwrite PKGBUILD files.')
    parser.add_argument('-r', '--recursive', dest='recursive',
                        action='store_true', default=False,
                        help='Recursively import dependencies')
    parser.add_argument('-u', '--update', dest='update',
                        action='store_true', default=False,
                        help='Update PKGBUILD if a newer version is found.')
    args = parser.parse_args()

    # Dictionary containing valid Python versions
    valid_python_versions = {"kinetic": ["2.7", "3.7"],
                             "melodic": ["2.7", "3.7"]}

    # Default Python version that will be used
    # Even though the official python version for melodic is stil 2.7, the official one for Arch is 3.
    default_python_version = {"kinetic": "2.7",
                              "melodic": "3.7"}

    python_version = default_python_version[args.distro]
    if args.python_version != "":
        if args.python_version in valid_python_versions[args.distro]:
            python_version = args.python_version
        else:
            print("Invalid Python version (%s) for %s, using version %s instead."
                  % args.python_version % args.distro % python_version)

    distro = DistroDescription(args.distro,
                               python_version=python_version,
                               url=args.distro_url % args.distro)

    if args.output_directory:
        output_directory = os.path.expanduser(args.output_directory)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        if os.path.isdir(output_directory):
            distro_dir = os.path.abspath(output_directory)
        else:
            print("Invalid --output-directory. Exiting.")
            sys.exit(1)
    else:
        distro_dir = None
        print("Missing mandatory --output-directory. Exiting.")
        sys.exit(1)

    if args.list_packages:
        list_packages(distro, distro_dir)
        return

    if not args:
        parser.error('No package specified.')

    generated = set()

    # Dump file containing the ordered list of packages to install
    distro_makepkg_filename = makepkg_filename % {'distro': args.distro}
    written = {"directory": distro_dir,
               "packages": list()}

    if os.path.isfile(distro_makepkg_filename):
        makepkg_dump = open(distro_makepkg_filename, "rb")
        written = pickle.load(makepkg_dump)
        makepkg_dump.close()

    # Dump file containing previously generated packages
    distro_generated_filename = updated_packages_filename % {'distro': args.distro}

    if os.path.isfile(distro_generated_filename):
        # Load dump of already updated packages to speedup updates
        print('Loading set of previously updated packages: %s'
              % (colored(distro_generated_filename, 'white',
                         attrs=['bold'])))
        updated_packages_dump = open(distro_generated_filename, "rb")
        generated = pickle.load(updated_packages_dump)
        updated_packages_dump.close()
        for package in sorted(generated):
            print('Ignoring %s'
                  % (colored(package, 'yellow', attrs=['bold'])))

    try:
        for package in args.package:
            generate_pkgbuild(distro, distro.package(package), distro_dir,
                              exclude_dependencies=args.exclude_dependencies.split(','),
                              force=args.force,
                              no_overwrite=args.no_overwrite,
                              update=args.update,
                              recursive=args.recursive,
                              rosdep_urls=args.rosdep_urls,
                              generated=generated,
                              written=written)
    except KeyboardInterrupt:
        pass

    if not os.path.exists(updates_packages_dir):
        os.makedirs(updates_packages_dir)

    makepkg_dump = open(distro_makepkg_filename, "wb")
    updated_packages_dump = open(distro_generated_filename, "wb")
    pickle.dump(generated, updated_packages_dump)
    pickle.dump(written, makepkg_dump)
    updated_packages_dump.close()
    makepkg_dump.close()


if __name__ == '__main__':
    main()
