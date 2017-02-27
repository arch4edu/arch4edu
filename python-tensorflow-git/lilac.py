#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'pkgdesc' in line:
        print(line.replace('."','.(added support for NVIDIA GPUs with compute capability 5.2,6.1)"'))
    elif 'makedepends' in line:
        print(line.replace(')',' "cuda" "cudnn")'))
    elif 'TF_CUDA_COMPUTE_CAPABILITIES' in line:
        print('    export TF_CUDA_COMPUTE_CAPABILITIES="5.2,6.1"')
    elif 'TF_ENABLE_XLA' in line:
        print(line.replace('1','0'))
    elif './configure' in line:
        print('  yes "" |'+line)
    else:
        print(line)

  import os
  os.environ['http_proxy']='127.0.0.1:8123'

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
