#!/usr/bin/env python3
from lilaclib import *

update_on = [{'archpkg': 'pypy'}]
build_prefix = ['extra-armv6h', 'extra-armv7h']
time_limit_hours = 72

def pre_build():
    download_official_pkgbuild('pypy3')
    add_arch(['armv6h', 'armv7h'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('source=('):
            print(line.replace('(', '(a243e4e0b21c.patch::"https://bitbucket.org/pypy/pypy/commits/a243e4e0b21c968ba3fb42e3a575be24a2d6461b/raw"\n'))
        elif line.startswith('sha512sums=('):
            print(line.replace('(', '("480e1e9fc11d703ad167ca0fe9473e5216b02f2b39a1251ac9f673252d65a7837cbbcfbebba8a941542ef5c044cb6021b83cec218cdede12b3cfd2fa28e5dff2"\n'))
        elif line.startswith('  patch'):
            print(line)
            print('  patch -Np1 -i ${srcdir}/a243e4e0b21c.patch')
        else:
            print(line)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main('extra-x86_64')
