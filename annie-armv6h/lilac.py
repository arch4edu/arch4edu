#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'annie'}]
build_prefix = 'action-extra-armv6h'

def pre_build():
    aur_pre_build('annie')
    add_arch(['armv6h'])

post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
