#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
repo_depends = ['ccache-ext']
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('#') and not line.startswith('# '):
            print(line[1:])
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
