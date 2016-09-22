#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'multilib'
def pre_build():
    aur_pre_build()
    import os
    os.environ['https_proxy']='127.0.0.1:8123'
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
