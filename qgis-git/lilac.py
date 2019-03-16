#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'github': 'qgis/QGIS'}]
build_prefix = 'extra-x86_64'
depends = ['grass']

def pre_build():
    aur_pre_build()
    add_depends(['qt5-xmlpatterns'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
