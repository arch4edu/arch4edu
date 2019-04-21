#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = ['extra-x86_64', 'extra-aarch64']
time_limit_hours = 4

def pre_build():
    aur_pre_build()
    add_arch(['armv6h', 'armv7h', 'aarch64'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('depends=('):
            print(line.replace('\\', ' "qt5-location" "qt5-svg"'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
