#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
def pre_build():
    aur_pre_build()
    add_depends(['gtest'])
    for line in edit_file('PKGBUILD'):
        if 'conflicts' in line:
            print('provides=(zoltan)')
            print(line.replace('gtest','zoltan'))
        elif 'cmake .. -DTrilinos' in line:
            print('export FFLAGS+=" -fallow-argument-mismatch -fallow-invalid-boz"')
            print('export CFLAGS+=" -fcommon"')
            print(line)
        elif 'make VERBOSE' in line:
            print('make -j4')
        elif 'make DESTDIR' in line:
            print(line)
            print('rm $pkgdir/usr/lib/libgtest.so')
            print('rm -rf $pkgdir/usr/include/gtest')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
