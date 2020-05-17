#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'qgroundcontrol'}]
build_prefix = 'extra-aarch64'
repo_depends = [('fakeroot-tcp-aarch64', 'fakeroot-tcp')]
time_limit_hours = 4

def pre_build():
    run_cmd(['sh', '-c', 'rm -f *.part'])
    aur_pre_build('qgroundcontrol')
    add_arch(['aarch64'])
    add_makedepends(['qt5-tools', 'qt5-x11extras', 'qt5-wayland'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main('extra-x86_64')
