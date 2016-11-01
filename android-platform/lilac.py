#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'multilib-arch4edu'
depends = ['android-sdk', 'android-sdk-platform-tools']
def pre_build():
    aur_pre_build()
    import os
    os.environ['https_proxy']='127.0.0.1:8123'
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
