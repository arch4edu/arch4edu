#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'PKGEXT=' in line:
        continue
    if 'http://www-us.apache.org/dist/|' in line:
        print(line.replace('http://www-us.apache.org/dist/|', 'https://mirrors.tuna.tsinghua.edu.cn/apache/'))
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
