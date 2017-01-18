#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'pkgdesc' in line:
        print(line.replace('."','.(added support for NVIDIA GPUs with compute capability 5.2,6.1)"'))
    elif 'makedepends' in line:
        print(line.replace(')',' "cuda" "cudnn" "hadoop")'))
    elif 'TF_CUDA_COMPUTE_CAPABILITIES' in line:
        print('    export TF_CUDA_COMPUTE_CAPABILITIES="5.2,6.1"')
    elif 'git describe' in line:
        print(line.replace('+','.'))
    elif './configure' in line:
        print('  export TF_NEED_GCP=0')
        print('  export TF_NEED_HDFS=1')
        print('  export CC=gcc-5')
        print('  echo -e "\\n\\n\\n"|'+line)
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
