#!/bin/bash

# Test if external packages for PETSC are installed

CONFOPTS=""

## External downloads
#for external_pkg in hypre; do
  #CONFOPTS="${CONFOPTS} --download-${external_pkg}=1"
#done

# HYPRE
if [ -f "/usr/lib/libHYPRE.so" ]; then
  CONFOPTS="${CONFOPTS} --with-hypre-lib=/usr/lib/libHYPRE.so --with-hypre-include=/usr/include/hypre"
fi

# Kokkos
if [ -f "/usr/lib/libkokkoscore.so" ]; then
 CONFOPTS="${CONFOPTS} --with-kokkos=1"
fi

# (Par)METIS
if [ -f "/usr/include/metis.h" ]; then
  CONFOPTS="${CONFOPTS} --with-metis=1"
  if [ -f "/usr/include/parmetis.h" ]; then
    CONFOPTS="${CONFOPTS} --with-parmetis=1"
  fi
fi

# MUMPS
if [ -f "/usr/lib/libmumps_common.so" ]; then
  CONFOPTS="${CONFOPTS} --with-mumps=1"
fi

# ScaLAPACK
if [ -f "/usr/lib/pkgconfig/scalapack.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-scalapack=1"
fi

# SuperLU_DIST
if [ -f "/usr/lib/pkgconfig/superlu_dist.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-superlu_dist-lib=-lsuperlu_dist --with-superlu_dist-include=/usr/include/superlu_dist"
fi

# Triangle
if [ -f "/usr/lib/libtriangle.so" ]; then
  CONFOPTS="${CONFOPTS} --with-triangle=1"
fi

# Zoltan
if [ -f "/usr/lib/libzoltan.so" ]; then
  CONFOPTS="${CONFOPTS} --with-zoltan=1"
fi

echo "${CONFOPTS}"
