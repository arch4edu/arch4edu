#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
# depends = []

def pre_build():
  # obtain base PKGBUILD, e.g.
  aur_pre_build('python-tensorflow-git')

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'pkgname=' in line:
        print('pkgname=python-tensorflow-gpu5.2-git')
    elif 'pkgdesc' in line:
        print(line.replace('."','.(support NVIDIA GPUs with Compute Capability 5.2)"'))
    elif 'depends' in line:
        print(line.replace(')',' "cuda" "cudnn")'))
    elif 'pkgver()' in line:
        print('optdepends=()')
        print(line)
    elif 'conflicts' in line:
        print(line.replace(')',' "python-tensorflow-git" "python-tensorflow-nogpu-git")'))
    elif 'TF_CUDA_COMPUTE_CAPABILITIES' in line:
        print('    export TF_CUDA_COMPUTE_CAPABILITIES=5.2')
    elif './configure' in line:
        print('  export TF_NEED_GCP=0')
        print('  export CC=gcc-5')
        print('  export CXX=g++-5')
        print('  echo -e "/usr/lib/python3.5/site-packages"|'+line)
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  aur_post_build()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
