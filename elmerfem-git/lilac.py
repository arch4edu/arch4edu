#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Winston Wu <winstonwu91@gmail.com>'}]
update_on = [{'github': 'ElmerCSC/elmerfem'}]
build_prefix = 'extra-x86_64'
time_limit_hours = 8
repo_depends = ['paraview-opt','mumps-par','oce','hypre','mmg3d','libnn-git','libcsa-git','scalapack','trilinos']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
