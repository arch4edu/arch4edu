#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('_build_opt=1'):
            pass
        elif line.startswith('build() {'):
            print(line)
            print('  export https_proxy=http://127.0.0.1:7890')
        else:
            print(line)
