#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
repo_depends = ['sphinxbase']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'python3.6' in line:
            print(line.replace('python3.6', 'python3.7'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
