#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-aarch64'
time_limit_hours = 24

def pre_build():
    download_official_pkgbuild('pypy3')
    add_arch(['aarch64'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main('extra-x86_64')
