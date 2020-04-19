#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('sha256sums=('):
            print(line.replace('2bffdbc2a02f3bc69ab59a8ff881c75abe83d3064dc59bf8be261d638cd1afe0', '8ba26f0c3a5928e7860e905520dfd4b49d81d65d170ae111bd9ddf24eea330e7'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
