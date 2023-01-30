#!/bin/bash

# Test if external packages for PETSC are installed

CONFOPTS=""

## External downloads
#for external_pkg in hypre; do
  #CONFOPTS="${CONFOPTS} --download-${external_pkg}=1"
#done

# FFTW
if [ -f "/usr/lib/pkgconfig/fftw3.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-fftw=1"
fi

# HDF5
if [ -f "/usr/lib/pkgconfig/hdf5.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-hdf5=1 --download-hdf5-fortran-bindings=1"
fi

# HYPRE
if [ -f "/usr/lib/libHYPRE.so" ]; then
  CONFOPTS="${CONFOPTS} --with-hypre-lib=/usr/lib/libHYPRE.so --with-hypre-include=/usr/include/hypre"
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

# PaStiX https://gitlab.com/petsc/petsc/-/issues/1259
#if [ -f "/usr/lib/pkgconfig/pastic.pc" ]; then
#  CONFOPTS="${CONFOPTS} --with-pastix=1"
#fi

# ScaLAPACK
if [ -f "/usr/lib/pkgconfig/scalapack.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-scalapack=1"
fi

# Scotch
if [ -f /usr/include/scotch.h ]; then
  SCOTCH_LIBS="libesmumps.so,libptscotch.so,libptscotcherr.so,libscotch.so,libscotcherr.so"
  # Include bzip2 if scotch was build with bzip2 support
  if [ -f /usr/include/bzlib.h ];then
    SCOTCH_LIBS="${SCOTCH_LIBS},libbz2.so"
  fi
  SCOTCH_LIBS="[${SCOTCH_LIBS}]"
  CONFOPTS="${CONFOPTS} --with-ptscotch=1 --with-ptscotch-lib=${SCOTCH_LIBS} --with-ptscotch-include=${SCOTCH_DIR}"
fi

# SuiteSparse
if [ -f "/usr/include/SuiteSparse_config.h" ]; then
  CONFOPTS="${CONFOPTS} --with-suitesparse=1"
fi

# SuperLU
if [ -f "/usr/lib/pkgconfig/superlu.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-superlu-lib=-lsuperlu --with-superlu-include=/usr/include/superlu"
fi

# SuperLU_DIST
if [ -f "/usr/lib/pkgconfig/superlu_dist.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-superlu_dist-lib=-lsuperlu_dist --with-superlu_dist-include=/usr/include/superlu_dist"
fi

# Triangle
if [ -f "/usr/lib/libtriangle.so" ]; then
  CONFOPTS="${CONFOPTS} --with-triangle=1"
fi

# Trilinos (ML)
if [ -f "/usr/lib/libml.so" ]; then
  CONFOPTS="${CONFOPTS} --with-ml=1"
  # Add boost support (may be useful for trilinos)
  CONFOPTS="${CONFOPTS} --with-boost=1"
fi

echo "${CONFOPTS}"
