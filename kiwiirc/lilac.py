#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'github': 'kiwiirc/kiwiirc'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build(do_vcs_update=True)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
