SGE_ROOT=/opt/sge
export SGE_ROOT
[ -d $SGE_ROOT/bin/lx-amd64 ] && PATH=$PATH:$SGE_ROOT/bin/lx-amd64
export PATH
