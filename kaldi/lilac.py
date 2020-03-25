#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'github': 'kaldi-asr/kaldi'}]
build_prefix = 'extra-x86_64'
repo_depends = ['cub', 'gcc7', ('gcc7', 'gcc7-libs'), 'kaldi-openfst', 'openblas-lapack']

def pre_build():
    aur_pre_build(do_vcs_update=True)

    for line in edit_file('PKGBUILD'):
        if 'makedepends=(' in line:
            print(line.replace(')',' "cuda")'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
