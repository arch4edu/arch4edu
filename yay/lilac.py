#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = ['extra-x86_64', 'extra-armv6h', 'extra-armv7h', 'extra-aarch64']
time_limit_hours = 3
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
