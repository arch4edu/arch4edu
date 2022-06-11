#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
repo_depends = ['scotch']
build_prefix = 'extra-x86_64'
def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'arch=' in line:
            print(line)
            print('depends=(scotch)')
        elif 'mmg-$pkgver' in line:
            print(line)
            print('export CFLAGS+=" -fcommon"')
            print('export CXXFLAGS+=" -fcommon"')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
