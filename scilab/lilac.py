#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
repo_depends = ['apache-lucene', 'bwidget', 'fop-hyph', 'java-flexdock', 'java-qdox', 'java-skinlf', 'java-testng', 'javahelp2', 'jeuclid-core', 'jgoodies-looks', 'jgraphx', 'jlatexmath-fop', 'jogl', 'jrosetta', 'saxon-he']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'java-environment' in line:
            print(line.replace('>=8', '=8'))
        elif './configure' in line:
            print('  ./configure --with-jdk=/usr/lib/jvm/java-8-openjdk \\')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
