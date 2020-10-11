#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
repo_depends = ['scotch','scalapack','parmetis']
build_prefix = 'extra-x86_64'
def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'alllib' in line:
            print('export CFLAGS+=" -fallow-argument-mismatch"')
            print(line)
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
