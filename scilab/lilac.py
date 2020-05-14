#!/usr/bin/env python3
from lilaclib import *

from pyalpm import Handle
arch = 'x86_64'
package = 'jre8-openjdk'
dbpath = '/var/lib/archbuild/extra-x86_64/root/var/lib/pacman/'
gpgpath = '/var/lib/archbuild/extra-x86_64/root/etc/pacman.d/gnupg'
mirror = 'https://mirrors.tuna.tsinghua.edu.cn/archlinux'
handle = Handle('/', dbpath)
for i in ['core', 'extra', 'community']:
    repo = handle.register_syncdb(i, 0)
for repo in handle.get_syncdbs():
    result = repo.get_pkg(package)
    if result:
        url = f'{mirror}/{repo.name}/os/{arch}/{result.filename}'
        break

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
repo_depends = ['apache-lucene', 'bwidget', 'fop-hyph', 'java-flexdock', 'java-qdox', 'java-skinlf', 'java-testng', 'javahelp2', 'jeuclid-core', 'jgoodies-looks', 'jgraphx', 'jlatexmath-fop', 'jogl', 'jrosetta', 'saxon-he']
build_prefix = 'extra-x86_64'
makechrootpkg_args = ['-I', 'tmp/'+result.filename]

def pre_build():
    aur_pre_build()

    run_cmd(['wget', '-nc', url, url+'.sig'])
    run_cmd(['gpg', '--homedir', gpgpath, '--verify', result.filename+'.sig', result.filename])
    run_cmd(['mkdir', '-p', 'tmp'])
    run_cmd(['mv', result.filename, result.filename+'.sig', 'tmp'])

    for line in edit_file('PKGBUILD'):
        if 'java-environment' in line:
            print(line.replace('>=8', '=8'))
        elif './configure' in line:
            print('  ./configure --with-jdk=/usr/lib/jvm/java-8-openjdk \\')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
