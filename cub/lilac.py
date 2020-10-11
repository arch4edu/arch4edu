#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        print(line.replace('f464eda366e4dfe0c1d9ae2a6bbc22c5804cf131f8a67974c01fae4ae8213e8b', '7c3784cf59f02d4a88099d6a11e357032bac9eac2b9c78aaec947d1270e21871'))

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
