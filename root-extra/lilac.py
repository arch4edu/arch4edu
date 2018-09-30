#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['cern-vdt', 'pythia', 'root']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'makedepends=(' in line:
            print(line.replace(')', ' "blas" "go" "gcc-fortran" "ocaml" "python-numpy" "tcsh" "z3")'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
