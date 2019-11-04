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

install_ros_stack() {
  if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: install_ros_stack <src-dir> <ros-dir>"
    exit 1
  fi
  
  mkdir -p $pkgdir/$2
  cp -r $1/* $pkgdir/$2
  find $pkgdir/$2 -name manifest.xml -printf '%h/build\n' | xargs rm -rf
  fix_rpaths $1 $2
}

fix_rpaths() {
  if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: fix_rpaths <src-dir> <ros-dir>"
    exit 1
  fi

  executables=$(find $pkgdir/$2 -type f -executable)
  for file in $executables; do
    rpath_output=$(chrpath -l $file 2>/dev/null || echo "")
    if [ -n "$rpath_output" ] && echo $rpath_output | grep RPATH; then
      fixed_rpath=$(echo $rpath_output | sed 's/.*RPATH=//g' | sed "s?$1?$2?g")
      chrpath -r $fixed_rpath $file
    fi
  done
}

