#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['gyp-git']
def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line[0:9]=='depends=(':
            print(line.replace(')',' nss)'))
        elif 'makedepends=(' in line:
            print(line.replace(')',' "gtk2")'))
        else:
            print(line)
    import os
    os.environ['http_proxy']='127.0.0.1:8123'
post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
