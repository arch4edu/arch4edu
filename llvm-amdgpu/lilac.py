#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build
time_limit_hours = 4
build_args = ['-r', os.path.expanduser('~/.lilac/archbuild')]
makepkg_args = ['--nocheck']

if __name__ == '__main__':
    single_main(build_prefix)
