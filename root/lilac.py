#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['cern-vdt', 'llvm50', 'pythia', 'xrootd']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'makedepends=(' in line:
            print(line.replace(')', ' "blas" "fcgi" "go" "gcc-fortran" "ocaml" "pythia" "python-numpy" "tcsh" "xrootd" "z3")'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
