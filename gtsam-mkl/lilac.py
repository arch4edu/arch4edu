#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'gtsam'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build('gtsam')

    for line in edit_file('PKGBUILD'):
        if line == 'pkgname=gtsam':
            print(line + '-mkl')
        else:
            print(line.replace('$pkgname', 'gtsam').replace('${pkgname}', 'gtsam'))

    add_depends(['eigen', 'intel-tbb', 'intel-mkl'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
