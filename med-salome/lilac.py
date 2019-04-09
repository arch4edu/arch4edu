#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
repo_depends = ['hdf5_18-cpp-fortran']
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    add_makedepends(['cmake'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
