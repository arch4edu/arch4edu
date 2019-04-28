#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'ca1dc15e9f320983e4d53ccb947ce58729952728273fdf415ab309ea2c0cd7fa' in line:
            print(line.replace('ca1dc15e9f320983e4d53ccb947ce58729952728273fdf415ab309ea2c0cd7fa','43c64711301c2caf40dc56d7b91dd03d2b882a31fa31812bf20de0c8fb2e717f'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
