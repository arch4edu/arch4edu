#! /bin/bash

TMP_LLP=$LD_LIBRARY_PATH
if [ -z $TMP_LLP ] ; then
  LLP_NULL=true ;
else
  LLP_NULL=false ;
fi

if [ -f /opt/intel/composerxe/linux/bin/compilervars.sh ] ; then
. /opt/intel/composerxe/linux/bin/compilervars.sh <arch>
fi
#. /opt/intel/composerxe/bin/iccvars.sh <arch>

PATH=$PATH:/opt/intel/bin
export PATH

if [ $LLP_NULL ] ; then
  unset LD_LIBRARY_PATH
else
  LD_LIBRARY_PATH=$TMP_LLP
  export LD_LIBRARY_PATH
fi

export INTEL_LICENSE_FILE=/opt/intel/licenses
