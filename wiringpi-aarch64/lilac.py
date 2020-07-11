#!/bin/python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'github': 'archlinuxarm/PKGBUILDs', 'path': 'alarm/wiringpi'}]
build_prefix = 'extra-aarch64'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxarm/PKGBUILDs', 'alarm/wiringpi'])
    add_arch(['aarch64'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
