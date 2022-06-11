#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
repo_depends = [('fakeroot-tcp-armv6h', 'fakeroot-tcp')]
build_prefix = 'extra-armv6h'

def pre_build():
    aur_pre_build('github-actions-bin')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
