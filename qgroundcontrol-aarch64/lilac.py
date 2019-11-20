#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-aarch64'
time_limit_hours = 4

def pre_build():
    aur_pre_build()
    add_arch(['aarch64'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('\tpatch'):
            print('\tsed "s|so.56|so.*|g" -i ${srcdir}/${pkgname}-${pkgver}/QGCSetup.pri')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main('extra-x86_64')
