#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build()

    flag = False
    for line in edit_file('PKGBUILD'):
        if 'haswell' in line:
            flag = True
        if line.startswith('pkgname'):
            print('pkgname=python-pytorch-rocm')
        elif flag and 'python setup.py build' in line:
            print('#' + line)
        else:
            print(line)
