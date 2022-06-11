#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'
repo_depends = ['libmatio']
time_limit_hours = 8

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'depends=' in line:
            print(line.replace('netcdf','netcdf-openmpi'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
