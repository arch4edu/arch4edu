#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'github': 'baidu-research/warp-ctc'}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'makedepends' in line:
        print(line.replace(')',' "torch7-cutorch-git")'))
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
