#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'alias': 'python'}]
build_prefix = 'extra-x86_64'
repo_depends = ['ros-build-tools-py3', 'ros-noetic-catkin', 'ros-noetic-message-generation', 'ros-noetic-message-runtime', 'ros-noetic-std-msgs']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if "arch=('any')" in line:
            print('arch=("x86_64")')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
