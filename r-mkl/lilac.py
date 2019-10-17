#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}, {'aur': 'intel-mkl'}]
repo_depends = [('intel-parallel-studio-xe', 'intel-common-libs'), ('intel-parallel-studio-xe', 'intel-mkl'), ('intel-parallel-studio-xe', 'intel-openmp')]
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
