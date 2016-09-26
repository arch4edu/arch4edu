#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
def pre_build():
  aur_pre_build()
  for line in edit_file('PKGBUILD'):
    if 'pkgdesc=' in line:
        print(line[0:-1]+'. Built with eclipse-java."')
    elif line[0:8]=='depends=':
        print(line.replace('eclipse','eclipse-java'))
    elif 'prepare' in line:
        print(line)
        print('  export LANG=en_US.UTF-8')
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
