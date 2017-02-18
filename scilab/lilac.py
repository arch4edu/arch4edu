#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends=['apache-lucene', 'fop-hyph', 'java-flexdock', 'java-qdox', 'java-skinlf', 'java-testng', 'javahelp2', 'jeuclid-core', 'jgoodies-looks', 'jgraphx', 'jlatexmath-fop', 'jogl', 'jrosetta', 'saxon-he']

def pre_build():
    aur_pre_build()
    import os
    os.environ['JAVA_HOME']='/usr/lib/jvm/default'

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
