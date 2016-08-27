#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['openblas-lapack', ('python-scikit-image','python2-scikit-image'), 'python2-leveldb']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
