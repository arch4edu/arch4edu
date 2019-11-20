#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}, {'github': 'WiringPi/WiringPi-Python'}]
build_prefix = 'extra-aarch64'
makechrootpkg_args = ['-D', '/etc/ca-certificates/extracted']

def pre_build():
    aur_pre_build()
    add_arch(['aarch64'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
