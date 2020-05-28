#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'ccnet-server'}]
build_prefix = 'extra-aarch64'
repo_depends = [('libsearpc-aarch64', 'libsearpc'), ('fakeroot-tcp-aarch64', 'fakeroot-tcp')]

def pre_build():
    aur_pre_build('ccnet-server')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
