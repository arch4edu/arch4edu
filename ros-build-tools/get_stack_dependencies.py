#!/usr/bin/env python3
# Copyright (c) 2012, Lorenz Moesenlechner <moesenle@in.tum.de>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Intelligent Autonomous Systems Group/
#       Technische Universitaet Muenchen nor the names of its contributors 
#       may be used to endorse or promote products derived from this software 
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import xml.dom.minidom as minidom
import sys


def main():
  if len(sys.argv) < 2:
    print('Usage: %s <stack.xml>' % sys.argv[0])
    return 1

  top_level = minidom.parse(sys.argv[1])
  if len(top_level.childNodes) != 1 or top_level.childNodes[0].nodeName != 'stack':
    print('Invalid stack.xml. No <stack> node found on toplevel.')
    return 1
  stack = top_level.childNodes[0]
  legacy_dependency_nodes = [n for n in stack.childNodes if n.nodeName == 'depend']
  if legacy_dependency_nodes:
    print(*[n.getAttribute('stack') for n in legacy_dependency_nodes],
         sep=' ', end='')
  else:
    dependencies = [n.firstChild.wholeText for n in stack.childNodes
                    if n.nodeName == 'depends']
    print(*dependencies, sep=' ', end='')


if __name__ == '__main__':
  main()
