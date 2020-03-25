#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'github': 'numba/llvmlite'}, {'alias': 'python'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('depends=('):
            print(line.replace('llvm', 'llvm7'))
        elif line.startswith('makedepends=('):
            print(line.replace('llvm', 'llvm7'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
