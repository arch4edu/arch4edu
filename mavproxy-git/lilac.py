#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}, {'github': 'Dronecode/MAVProxy'}]
build_prefix = 'extra-x86_64'
repo_depends = ["python2-pymavlink-git"]

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'depends=(' in line:
        print(line)
        print('makedepends=("python2-setuptools" "git")')
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
