#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'python-pigpio'}]
build_prefix = 'extra-armv6h'

def pre_build():
    aur_pre_build('python-pigpio')
    add_arch(['armv6h'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
