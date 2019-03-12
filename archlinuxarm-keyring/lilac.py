#!/bin/python3
from lilaclib import *

update_on = [{'github': 'archlinuxarm/PKGBUILDs', 'path': 'core/archlinuxarm-keyring'}]
build_prefix = 'extra-x86_64'
makepkg_args = ['--skippgpcheck']

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxarm/PKGBUILDs', 'core/archlinuxarm-keyring'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
