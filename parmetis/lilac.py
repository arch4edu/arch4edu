#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgdirname='):
            print(line.replace('73dab469aa36', '475d8facbb32'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
