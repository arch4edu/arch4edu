#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('build()'):
            print('  export https_proxy=127.0.0.1:8123')
        else:
            print(line)
