#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'github': 'arch4edu/devtools-arch4edu-extra'}]
repo_depends = [('fakeroot-tcp-armv7h', 'fakeroot-tcp')]
build_prefix = 'extra-armv7h'
pre_build = vcs_update

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
