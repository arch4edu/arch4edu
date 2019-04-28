#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}, {'github': 'ArduPilot/pymavlink'}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'makedepends' in line:
        print(line.replace(')',' "python2-setuptools" "python2-lxml")'))
    elif 'depends' in line:
        print(line.replace(')',' "python2-future")'))
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
