#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends = ['kaldi']

def pre_build():
    aur_pre_build()
    run_cmd(['rm', '-f', 'master.zip'])

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
