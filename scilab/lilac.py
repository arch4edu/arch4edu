#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['apache-lucene', 'bwidget', 'fop-hyph', 'java-flexdock', 'java-qdox', 'java-skinlf', 'java-testng', 'javahelp2', 'jeuclid-core', 'jgoodies-looks', 'jgraphx', 'jlatexmath-fop', 'jogl', 'jrosetta', 'saxon-he']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'java-enviroment' in line or 'java-runtime' in line:
            print(line.replace('>=8', '=8'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
