#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'rpiusbboot-git'}, {'github': 'raspberrypi/usbboot'}]
repo_depends = ['fakeroot-tcp']
build_prefix = 'extra-armv7h'

def pre_build():
    aur_pre_build('rpiusbboot-git')
    add_arch(['armv7h'])
    add_makedepends(['git'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
