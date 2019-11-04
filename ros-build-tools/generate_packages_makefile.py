#!/usr/bin/env python

import os.path
import subprocess
import sys


MAKEFILE_TARGET = """
.PHONY : %(package)s
%(package)s: %(package)s/%(output_file)s

%(package)s/%(output_file)s: %(dependency_string)s
\tcd %(package)s; makepkg -i
"""


class InvalidPackage(Exception):
  def __init__(self, package):
    self.package = package

  def __str__(self):
    return repr(self.package)


class Dependency(object):

  def __init__(self, directory_name, package_name, dependencies, output_file):
    self.directory_name = directory_name
    self.package_name = package_name
    self.dependencies = dependencies
    self.output_file = output_file


class DependencyCache(object):

  def __init__(self):
    self._dependencies = {}

  def add_package_directory(self, name):
    pkgbuild_file = os.path.realpath(name + '/PKGBUILD')
    if not os.path.exists(pkgbuild_file):
      raise InvalidPackage(name)
    aur_package_name = get_package_name(pkgbuild_file)
    if len(aur_package_name) == 0:
      raise InvalidPackage(name)
    dependencies = get_dependencies(pkgbuild_file)
    output_file = get_pkgbuild_output_file(pkgbuild_file)
    self._dependencies[aur_package_name] = Dependency(
      name, aur_package_name, dependencies, output_file)

  def get_package_names(self):
    return list(self._dependencies.keys())

  def get_packages(self):
    return list(self._dependencies.values())

  def get_package(self, name):
    return self._dependencies[name]

  def get_package_directory_name(self, name):
    return self._dependencies[name].directory_name

  def get_dependencies(self, package_name, remove_unknown=True):
    package_dependencies = self._dependencies.get(package_name)
    if package_dependencies is None:
      raise InvalidPackage(package_name)
    if not remove_unknown:
      return package_dependencies
    return [self._dependencies[dependency] for dependency in package_dependencies.dependencies
            if self._dependencies.get(dependency)]


def get_pkgbuild_variable(pkgbuild, variable, is_array=False):
  if is_array:
    array_string = '[@]'
  else:
    array_string = ''
  with subprocess.Popen(
      'source %s && echo ${%s%s}' % (pkgbuild, variable, array_string),
      shell=True, stdout=subprocess.PIPE) as shell_process:
    if is_array:
      return shell_process.stdout.readline().decode().split()
    else:
      return shell_process.stdout.readline().decode().strip()


def get_pkgbuild_output_file(pkgbuild):
  with subprocess.Popen(
      'source %s && echo ${pkgname}-${pkgver}-${pkgrel}-${HOSTTYPE}.pkg.tar.xz' % (pkgbuild),
      shell=True, stdout=subprocess.PIPE) as shell_process:
    return shell_process.stdout.readline().decode().strip()


def get_dependencies(pkgbuild):
  return get_pkgbuild_variable(pkgbuild, 'depends', is_array=True)


def get_package_name(pkgbuild):
  return get_pkgbuild_variable(pkgbuild, 'pkgname')


def generate_makefile(cache):
  makefile = """
all: %s
""" % ' '.join(['%s/%s' % (package.directory_name, package.output_file)
                for package in cache.get_packages()])

  for package in cache.get_package_names():
    dependency_string = ' '.join(['%s/%s' % (dependency.directory_name, dependency.output_file)
                                  for dependency in cache.get_dependencies(package)])
    makefile += MAKEFILE_TARGET % {'package': cache.get_package_directory_name(package),
                                   'output_file': cache.get_package(package).output_file,
                                   'dependency_string': dependency_string}
  return makefile
  
  
def main():
  if len(sys.argv) < 2:
    print('Usage: %s <AUR package>*' % sys.argv[0])
    return 1

  dependency_cache = DependencyCache()
  for arg in sys.argv[1:]:
    dependency_cache.add_package_directory(arg)

  print(generate_makefile(dependency_cache))


if __name__ == '__main__':
  main()
