#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = 'arch4edu-x86_64'
depends = ['openblas-lapack', 'python-scikit-image','python-pydotplus', 'python-leveldb']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
