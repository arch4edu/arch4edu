#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}, {'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'cmake ..' in line:
            print('export FFLAGS+=" -fallow-argument-mismatch"')
            print(line)
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
