#!/usr/bin/env python3
from lilaclib import *
import os

build_prefix = 'extra-x86_64'
makechrootpkg_args = ['-D', os.path.realpath('cquery')]

def pre_build():
    run_cmd('sh update-submodules.sh cquery'.split(' '))
    aur_pre_build(do_vcs_update=False)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
