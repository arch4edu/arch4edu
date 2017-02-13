#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends = ['vtk-py3-qt4']

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'makedepends=(' in line:
        print(line.replace(')',' "openmpi" "gdal" "unixodbc" "tk" "ffmpeg" "jsoncpp" "gcc-libs")'))
    elif 'patch -p1 < ../python35-ast.patch' in line:
        print(line)
        print('   #To strip non-ascii characters from docs')
        print('   sed "166s/doc/doc.encode(\'ascii\',errors=\'ignore\').decode(\'ascii\')/" -i tvtk/indenter.py')
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
