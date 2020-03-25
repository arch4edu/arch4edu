#!/usr/bin/env python3
from lilaclib import *

from pyalpm import Handle
arch = 'x86_64'
package = 'hdf5-openmpi'
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

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}, {'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'alias': 'python'}]
repo_depends = ['med', 'parmetis', 'scotch']
makechrootpkg_args = ['-I', 'tmp/'+result.filename]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    run_cmd(['wget', '-nc', url, url+'.sig'])
    run_cmd(['gpg', '--homedir', gpgpath, '--verify', result.filename+'.sig', result.filename])
    run_cmd(['mkdir', '-p', 'tmp'])
    run_cmd(['mv', result.filename, result.filename+'.sig', 'tmp'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
