#!/bin/python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'github': 'lilydjwg/pid_children'}]
build_prefix = 'extra-x86_64'

def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'archlinuxcn/repo', 'archlinuxcn/pid_children-git'])
    run_cmd(['git', 'rm', '-f', 'lilac.yaml'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
