#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
repo_depends = ['ros-build-tools-py3', 'ros-melodic-catkin', 'ros-melodic-genmsg']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgver='):
            print(line.replace('0.4.16', '0.4.18'))
        elif line.startswith('sha256sums=('):
            print(line.replace('31d3b86a0e3c0517b743a5c74dc3fe4a533ea22fdd1481b7432aa5f7b7800a0d', 'b756554e39368467bcb7d564de3f475373d264c3133538a708f60d0bf8543736'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
