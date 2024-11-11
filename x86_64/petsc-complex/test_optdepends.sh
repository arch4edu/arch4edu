#!/bin/bash

# Test if external packages for PETSC are installed

CONFOPTS=""

## External downloads
#for external_pkg in hypre; do
#CONFOPTS="${CONFOPTS} --download-${external_pkg}=1"
#done

# Kokkos
if [ -f "/usr/lib/libkokkoscore.so" ]; then
  CONFOPTS="${CONFOPTS} --with-kokkos=1"
fi

# HYPRE
if [ -f "/usr/lib/libHYPRE.so" ]; then
  CONFOPTS="${CONFOPTS} --with-hypre-lib=/usr/lib/libHYPRE.so --with-hypre-include=/usr/include/hypre"
fi

# MUMPS
if [ -f "/usr/lib/libmumps_common.so" ]; then
  CONFOPTS="${CONFOPTS} --with-mumps=1"
fi

# triangle
if [ -f "/usr/lib/libtriangle.so" ]; then
  CONFOPTS="${CONFOPTS} --with-triangle=1"
fi

# ScaLAPACK
if [ -f "/usr/lib/pkgconfig/scalapack.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-scalapack=1"
fi

# METIS
if [ -f "/usr/include/metis.h" ]; then
  CONFOPTS="${CONFOPTS} --with-metis=1"
  # PARMETIS
  if [ -f "/usr/include/parmetis.h" ]; then
    CONFOPTS="${CONFOPTS} --with-parmetis=1"
  fi
fi

# Scotch
SCOTCH_DIR="/usr/include"
if [ -f "/usr/include/scotch.h" ]; then
  SCOTCH_LIBS="libesmumps.so,libptscotch.so,libptscotcherr.so,libscotch.so,libscotcherr.so"
  # Include bzip2 if scotch was build with bzip2 support
  if [ -f /usr/include/bzlib.h ]; then
    SCOTCH_LIBS="${SCOTCH_LIBS},libbz2.so"
  fi
  SCOTCH_LIBS="[${SCOTCH_LIBS}]"
  CONFOPTS="${CONFOPTS} --with-ptscotch=1 --with-ptscotch-lib=${SCOTCH_LIBS} --with-ptscotch-include=${SCOTCH_DIR}"
fi

# SuperLU_DIST
SUPERLU_DIST_DIR="/usr/include/superlu_dist"
if [ -d "${SUPERLU_DIST_DIR}" ]; then
  CONFOPTS="${CONFOPTS} --with-superlu_dist=1 --with-superlu_dist-lib=-lsuperlu_dist --with-superlu_dist-include=${SUPERLU_DIST_DIR}"
fi

# PaStiX
PASTIX_CONF=$(which pastix-conf)
if [ -f "${PASTIX_CONF}" ]; then
  PASTIX_DIR="$($PASTIX_CONF --incs | sed 's/-I//')"
  if [ ! -d ${PASTIX_DIR} ]; then
    PASTIX_DIR="[]"
  fi
  #PASTIX_LIBS="$($PASTIX_CONF --libs)"
  PASTIX_LIBS="[libpastix.a,librt.so,libhwloc.so,libpthread.a]"
  CONFOPTS="${CONFOPTS} --with-pastix=1 --with-pastix-lib=${PASTIX_LIBS} --with-pastix-include=${PASTIX_DIR}"
fi

# Zoltan
if [ -f "/usr/include/zoltan.h" ]; then
  CONFOPTS="${CONFOPTS} --with-zoltan=1"
fi

# ML (complex-scalar is not supported)
if [ -f "/usr/lib/libml.so" ]; then
  CONFOPTS="${CONFOPTS} --with-ml=0"
  # Add boost support (may be useful for trilinos)
  CONFOPTS="${CONFOPTS} --with-boost=1"
fi

# Valgrind
if [ -f "/usr/lib/pkgconfig/valgrind.pc" ]; then
  CONFOPTS="${CONFOPTS} --with-valgrind=1"
fi

echo "${CONFOPTS}"
