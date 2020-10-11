#!/bin/python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxarm/PKGBUILDs', 'core/archlinuxarm-keyring'])
    add_into_array('validpgpkeys', ['77193F152BDBE6A6', '68B3537F39A313B3E574D06777193F152BDBE6A6'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
