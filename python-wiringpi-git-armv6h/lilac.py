#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'python-wiringpi-git'}, {'github': 'WiringPi/WiringPi-Python'}]
build_prefix = 'extra-armv6h'
makechrootpkg_args = ['-D', '/etc/ca-certificates/extracted']

def pre_build():
    aur_pre_build('python-wiringpi-git')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
