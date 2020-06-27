#!/bin/python3
from lilaclib import *
from lilac2.pkgbuild import _get_package_version, get_srcinfo

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'github': 'moonman/MyPKGBUILDs', 'path': 'linux-raspberrypi4'}]
build_prefix = 'action-skip'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'moonman/MyPKGBUILDs', 'linux-raspberrypi4'])
    add_arch(['x86_64'])
    epoch, pkgver, pkgrel = _get_package_version(get_srcinfo())
    run_cmd(['wget', '-nc', f'https://olegtown.pw/Public/ArchLinuxArm/RPi4/kernel/linux-raspberrypi4-{pkgver}-{pkgrel}-aarch64.pkg.tar.xz'])
    run_cmd(['wget', '-nc', f'https://olegtown.pw/Public/ArchLinuxArm/RPi4/kernel/linux-raspberrypi4-headers-{pkgver}-{pkgrel}-aarch64.pkg.tar.xz'])

def post_build():
    git_commit()

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
