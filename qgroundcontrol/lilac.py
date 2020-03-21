#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    run_cmd(['rm', '*.part'])
    aur_pre_build()
    add_makedepends(['qt5-tools', 'qt5-x11extras', 'qt5-wayland'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main('extra-x86_64')
