#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'makedepends' in line:
            print(line.replace('java-environment=8', 'java-environment=7'))
        elif 'sed' in line and '1.8' in line:
            print(line.replace('1.8', '1.7'))
        else:
            print(line)

def post_build():
    run_cmd('git add -f plantuml.run'.split(' '))
    aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
