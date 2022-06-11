#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['hypre','lis']
def pre_build():
    aur_pre_build()
    add_depends(['proj','hypre','lis'])
    for line in edit_file('PKGBUILD'):
        if 'makedepends' in line:
            print('')
        elif 'depends=' in line:
            print(line.replace('netcdf','netcdf-openmpi'))
        elif 'configure' in line:
            print('export CFLAGS+=" -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H"')
            print('export CPPFLAGS+=" -I/usr/include/hypre"')
            print('export FFLAGS+=" -fallow-argument-mismatch"')
            print(line.replace('disable-mpi','enable-mpi'))
            print('sed -i "s/-Werror-implicit-function-declaration//g" Makefile')
            print('sed -i "s/-Werror-implicit-function-declaration//g" src/Makefile')
            print('sed -i "s/-Werror-implicit-function-declaration//g" modules/Makefile')
            print('sed -i "s/LIS_MATRIX_CRS/LIS_MATRIX_CSR/g" modules/lis.c')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
