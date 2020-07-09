#!/usr/bin/env python3
from lilaclib import *

maintainers = [
        {'github': 'migueldvb', 'email': 'Miguel de Val-Borro <miguel.deval@gmail.com>'},
        {'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}
        ]
update_on = [{'aur': None}, {'alias': 'python'}]
repo_depends = ['python-astropy', 'python-extension-helpers']
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
