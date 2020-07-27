#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('depends=('):
            print(line.replace('llvm', 'llvm9'))
        elif line.startswith('makedepends=('):
            print(line.replace('llvm', 'llvm9'))
        elif line.startswith('pkgname=(python-llvmlite-git python2-llvmlite-git)'):
            print('pkgname=python-llvmlite-git')
        else:
            print(line)
