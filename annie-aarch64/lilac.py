#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'annie'}]
build_prefix = 'extra-aarch64'

def pre_build():
    aur_pre_build('annie')
    add_arch(['aarch64'])

    with open('PKGBUILD', 'a') as f:
        f.write('export http_proxy=127.0.0.1:8123\n')
        f.write('export https_proxy=127.0.0.1:8123\n')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
