#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  # obtain base PKGBUILD, e.g.
  download_official_pkgbuild('festival')

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'pkgname=festival' in line:
        print('pkgname=festival-gcc5')
        print('_'+line)
    elif 'pkgdesc' in line:
        print(line[:-1]+' (built with gcc5 and add text2utt)"')
    elif 'depends=' in line:
        print(line.replace(')',' gcc5)'))
        print('provides=(\'festival\')')
        print('conflicts=(\'festival\')')
    elif 'pkgname' in line:
        print(line.replace("pkgname","_pkgname"))
    elif 'sed -i "s#examples bin doc#examples#" festival/Makefile' in line:
        print(line)
        print('  sed -e "s/CC=gcc/CC=gcc-5/" -e "s/CXX=gcc/CXX=gcc-5/" -i speech_tools/config/compilers/gcc_defaults.mak')
    elif 'text2wave' in line:
        print('  install -m755 examples/text2utt "$pkgdir"/usr/bin')
        print(line)
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  git_add_files('PKGBUILD')
  git_add_files('*.patch')
  git_commit()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
