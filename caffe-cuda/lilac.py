#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'alias': 'python'}]
build_prefix = 'extra-x86_64'
repo_depends = ['openblas-lapack', 'python-scikit-image','python-pydotplus', 'python-leveldb']
makepkg_args = ['--nocheck']

def pre_build():
    aur_pre_build()
    add_makedepends(['texlive-latexextra'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
