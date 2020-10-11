#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['gcc7', ('gcc7', 'gcc7-libs'), 'python-graphviz', ('intel-parallel-studio-xe', 'intel-common-libs'), ('intel-parallel-studio-xe', 'intel-compiler-base'), ('intel-parallel-studio-xe', 'intel-openmp')]
makechrootpkg_args = ['-D', '/opt/intel/licenses']
time_limit_hours = 4
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
