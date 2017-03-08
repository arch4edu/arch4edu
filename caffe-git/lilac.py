#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['opencv2', 'openblas-lapack', ('python-scikit-image','python2-scikit-image'), 'python2-leveldb']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if "'opencv'" in line:
            print(line.replace("'opencv'",'"opencv2"'))
        elif "makedepends=(" in line:
            print(line.replace(")",' "cudnn")'))
        elif "35fa1150f5a5b3909e96422f1efe10d43bdd8cef6c0c5d5528c53f0bc579dd74" in line:
            print(line.replace("35fa1150f5a5b3909e96422f1efe10d43bdd8cef6c0c5d5528c53f0bc579dd74","SKIP"))
        else:
            print(line)

    for line in edit_file('Makefile.config'):
        if "USE_CUDNN" in line:
            print(line.replace("#",""))
        elif "OPENCV_VERSION" in line:
            print(line.replace("3","2"))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
