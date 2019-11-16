#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}, {'alias': 'python'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('url='):
            print(line)
            print('makedepends=("python-setuptools" "python2-setuptools")')
        elif line.startswith('  depends=('):
            print(line.replace(" 'python-setuptools'", '').replace(" 'python2-setuptools'", ''))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
