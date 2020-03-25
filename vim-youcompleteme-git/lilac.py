#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}, {'github': 'Valloric/YouCompleteMe'}]
repo_depends = ['ncurses5-compat-libs']
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if not line.startswith('groups=('):
            print(line.replace('http://download.eclipse.org', 'https://mirrors.tuna.tsinghua.edu.cn/eclipse'))

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
