#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
repo_depends = [('archimedes-tools', 'triangle'), 'udunits','g2clib','hdf4']
build_prefix = 'extra-x86_64'
def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'lesstif' in line:
            print(line.replace('lesstif','openmotif'))
        elif '-fopenmp' in line:
            print(line.replace('-fopenmp', '-fopenmp -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H '))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
