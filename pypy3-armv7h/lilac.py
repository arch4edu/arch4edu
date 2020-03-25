#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'archpkg': 'pypy3'}]
build_prefix = 'extra-armv7h'
time_limit_hours = 24

def pre_build():
    download_official_pkgbuild('pypy3')
    add_arch(['armv7h'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main('extra-x86_64')
