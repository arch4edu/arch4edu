#!/bin/python3
from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    run_cmd(['wget', '-O', 'PKGBUILD', 'https://raw.githubusercontent.com/archlinuxcn/repo/master/vim-youcompleteme-git/PKGBUILD'])
    vcs_update()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main(build_prefix)
