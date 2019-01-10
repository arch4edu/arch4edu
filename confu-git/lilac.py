#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'github': 'Maratyszcza/confu'}]
build_prefix = 'arch4edu-x86_64'
depends = ['python-ninja-syntax', ('python-ninja-syntax', 'python2-ninja-syntax')]
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
