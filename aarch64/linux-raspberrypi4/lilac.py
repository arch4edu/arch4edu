#!/bin/python3
from lilaclib import *
from lilac2.pkgbuild import _get_package_version, get_srcinfo

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'action-extra-aarch64'
time_limit_hours = 3

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'moonman/MyPKGBUILDs', 'linux-raspberrypi4'])

def post_build():
    git_commit()

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
