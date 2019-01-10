#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = 'arch4edu-x86_64'
depends = [('intel-parallel-studio-xe', 'intel-compiler-base'), ('intel-parallel-studio-xe', 'intel-fortran-compiler'), ('intel-parallel-studio-xe', 'intel-mkl')]
makechrootpkg_args = ['-D', '/opt/intel/licenses']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'replaces' in line:
            continue
        elif 'sh build_python.sh python2'
            print('\t\t;')
        elif line.startswith('pkgname='):
            print("pkgname='python-scipy-mkl'")
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
