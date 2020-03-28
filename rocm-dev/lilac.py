#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
repo_depends = ['hcc', 'hip-hcc', 'rocm-cmake', 'rocm-comgr', ('rocm-opencl-runtime', 'rocm-device-libs'), 'rocm-smi', 'rocm-utils', 'rocprofiler', 'rocr-debug-agent', 'rocr-runtime', 'hsakmt-roct']
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
