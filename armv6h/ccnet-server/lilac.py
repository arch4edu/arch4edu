#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-armv6h'
repo_depends = [('libsearpc-armv6h', 'libsearpc'), ('fakeroot-tcp-armv6h', 'fakeroot-tcp')]

def pre_build():
    aur_pre_build('ccnet-server')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
