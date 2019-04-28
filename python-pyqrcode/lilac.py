#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build

def post_build():
    git_add_files(['PKGBUILD','LICENSE'])
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
