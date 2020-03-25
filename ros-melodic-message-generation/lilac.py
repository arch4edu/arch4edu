#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
repo_depends = ['ros-build-tools-py3', 'ros-melodic-catkin', 'ros-melodic-gencpp', 'ros-melodic-geneus', 'ros-melodic-genlisp', 'ros-melodic-genmsg', 'ros-melodic-gennodejs', 'ros-melodic-genpy']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
