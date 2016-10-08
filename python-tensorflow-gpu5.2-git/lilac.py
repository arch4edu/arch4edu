#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'

def pre_build():
  aur_pre_build('python-tensorflow-git')

  for line in edit_file('PKGBUILD'):
    if 'pkgname=' in line:
        print('pkgname=python-tensorflow-gpu5.2-git')
    elif 'pkgdesc' in line:
        print(line.replace('."','.(support NVIDIA GPUs with Compute Capability 5.2)"'))
    elif 'depends' in line:
        print(line.replace(')',' "cuda" "cudnn")'))
    elif 'pkgver()' in line:
        print('optdepends=()')
        print(line)
    elif 'conflicts' in line:
        print(line.replace(')',' "python-tensorflow-git" "python-tensorflow-nogpu-git" "python-tensorflow-gpu6.1-git")'))
    elif 'TF_CUDA_COMPUTE_CAPABILITIES' in line:
        print('    export TF_CUDA_COMPUTE_CAPABILITIES=5.2')
    elif './configure' in line:
        print('  export TF_NEED_GCP=0')
        print('  export TF_NEED_HDFS=0')
        print('  export CC=gcc-5')
        print('  echo -e "\\n\\n\\n"|'+line)
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
