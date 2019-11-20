#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'seafile'}]
build_prefix = 'extra-armv6h'
repo_depends = ['libsearpc-armv6h', 'ccnet-server-armv6h']

def pre_build():
    aur_pre_build('seafile')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
