#!/bin/python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'action-extra-aarch64'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxarm/PKGBUILDs', 'alarm/wiringpi'])
    add_arch(['aarch64'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
