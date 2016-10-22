#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['eclipse-emf', 'eclipse-gef']

def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if '_mirror=' in line:
      print('_mirror=http://mirrors.ustc.edu.cn/eclipse')
    else:
      print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
