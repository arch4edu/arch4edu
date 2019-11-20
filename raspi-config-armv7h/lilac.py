#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'raspi-config'}]
build_prefix = 'extra-armv7h'

def pre_build():
    aur_pre_build('raspi-config')
    add_makedepends(['git'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
