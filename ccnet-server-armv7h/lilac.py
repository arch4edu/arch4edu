#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-armv7h'
repo_depends = [('libsearpc-armv7h', 'libsearpc'), ('fakeroot-tcp-armv7h', 'fakeroot-tcp')]

def pre_build():
    aur_pre_build('ccnet-server')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
