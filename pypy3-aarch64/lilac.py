#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'archpkg': 'pypy3'}]
build_prefix = 'action-extra-aarch64'
time_limit_hours = 8

def pre_build():
    download_official_pkgbuild('pypy3')
    add_arch(['aarch64'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
