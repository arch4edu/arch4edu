#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['grass']
pre_build = vcs_update

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  
if __name__ == '__main__':
  single_main()
