#!/usr/bin/env python3
from lilaclib import *

update_on = [{'archpkg': 'pypy'}]
build_prefix = ['extra-armv6h', 'extra-armv7h', 'extra-aarch64']
time_limit_hours = 72

def pre_build():
    download_official_pkgbuild('pypy')
    add_arch(['armv6h', 'armv7h', 'aarch64'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
