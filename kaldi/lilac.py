#!/usr/bin/env python3

from lilaclib import *
import os

build_prefix = 'arch4edu-x86_64'
depends=['kaldi-openfst', 'openblas-lapack']

def pre_build():
    aur_pre_build()
    os.environ['https_proxy']='127.0.0.1:8123'

    for line in edit_file('PKGBUILD'):
        if 'makedepends=(' in line:
            print(line.replace(')',' "cuda")'))
        else:
            print(line)

def post_build():
    aur_post_build()
    del os.environ['https_proxy']

if __name__ == '__main__':
  single_main(build_prefix)
