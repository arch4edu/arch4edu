#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = 'arch4edu-x86_64'
depends = [('intel-parallel-studio-xe', 'intel-compiler-base'), ('intel-parallel-studio-xe', 'intel-fortran-compiler'), ('intel-parallel-studio-xe', 'intel-mkl')]
makechrootpkg_args = ['-D', '/opt/intel/licenses']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'build() {' in line:
            print(line)
            print('\texport __INTEL_PRE_CFLAGS="$__INTEL_PRE_CFLAGS -D__PURE_INTEL_C99_HEADERS__ -D_Float32=float -D_Float64=double -D_Float128=\\"long double\\" -D_Float32x=_Float64 -D_Float64x=_Float128"')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
