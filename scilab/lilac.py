#!/usr/bin/env python3
from lilaclib import *
from pyalpm import Handle

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
repo_depends = ['apache-lucene', 'bwidget', 'fop-hyph', 'java-flexdock', 'java-qdox', 'java-skinlf', 'java-testng', 'javahelp2', 'jeuclid-core', 'jgoodies-looks', 'jgraphx', 'jlatexmath-fop', 'jogl', 'jrosetta', 'saxon-he']
build_prefix = 'extra-x86_64'
makechrootpkg_args = []

def download_package(package, arch='x86_64'):
    global makechrootpkg_args

    dbpath = f'/var/lib/archbuild/extra-{arch}/root/var/lib/pacman/'
    gpgpath = f'/var/lib/archbuild/extra-{arch}/root/etc/pacman.d/gnupg'
    mirror = 'https://mirrors.tuna.tsinghua.edu.cn/archlinux'
    handle = Handle('/', dbpath)
    for i in ['core', 'extra', 'community']:
        repo = handle.register_syncdb(i, 0)

    for repo in handle.get_syncdbs():
        result = repo.get_pkg(package)
        if result:
            if arch == 'x86_64':
                url = f'{mirror}/{repo.name}/os/{arch}/{result.filename}'
            makechrootpkg_args += ['-I', 'tmp/'+result.filename]
            break

    run_cmd(['wget', '-nc', '-P', 'tmp', url, url+'.sig'])
    run_cmd(['gpg', '--homedir', gpgpath, '--verify', 'tmp/'+result.filename+'.sig', 'tmp/'+result.filename])


def pre_build():
    aur_pre_build()

    download_package('jre-openjdk-headless')
    download_package('jre-openjdk')

    for line in edit_file('PKGBUILD'):
        if './configure' in line:
            print('  ./configure --with-jdk=/usr/lib/jvm/java-8-openjdk \\')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
