#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['libtinfo5']

def pre_build():
    aur_pre_build()
    run_cmd('sh update-submodules.sh cquery'.split(' '))

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
