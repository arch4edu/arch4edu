#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'yay'}]
build_prefix = 'extra-aarch64'
time_limit_hours = 3

def pre_build():
    aur_pre_build('yay')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
