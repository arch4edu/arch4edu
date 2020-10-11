#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['python-pytest-astropy-header', 'python-pytest-doctestplus', 'python-pytest-remotedata', 'python-pytest-openfiles', 'python-pytest-arraydiff', 'python-pytest-filter-subpackage']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
