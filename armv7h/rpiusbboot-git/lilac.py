#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'action-extra-armv7h'

def pre_build():
    aur_pre_build('rpiusbboot-git')
    add_arch(['armv7h'])
    add_makedepends(['git'])

post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
