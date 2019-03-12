#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = ['extra-armv6h', 'extra-armv7h', 'extra-aarch64']

def pre_build():
    aur_pre_build()
    add_arch(['aarch64'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
