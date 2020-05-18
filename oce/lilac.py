#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
time_limit_hours = 8
def pre_build():
    aur_pre_build()
    add_depends(['vtk','glew'])
    for line in edit_file('PKGBUILD'):
        if 'DOCE_WITH_GL2PS' in line:
            print(line.replace('OFF','ON'))
        elif 'DOCE_WITH_VTK' in line:
            print(line.replace('OFF','ON'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
