#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
update_on = [{'github': 'heavysink/aur', 'path': 'mpich-arch4edu'}]
build_prefix = 'extra-x86_64'
def pre_build():
    run_cmd(['sh', 'download-files-from-github.sh', 'heavysink/aur', 'mpich-arch4edu'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
