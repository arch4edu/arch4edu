#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['confu-git', 'nccl', 'python-peachpy-git', 'python-scikit-image', 'python-lmdb', 'python-leveldb', 'python-glog', 'python-nvd3']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
