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

# METIS
if [ -f "/usr/include/metis.h" ]; then
  CONFOPTS="${CONFOPTS} --with-metis=1"
  # PARMETIS
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
SUPERLU_DIST_DIR="/usr/include/superlu_dist"
if [ -d "${SUPERLU_DIST_DIR}" ]; then
  CONFOPTS="${CONFOPTS} --with-superlu_dist=1 --with-superlu_dist-lib=-lsuperlu_dist --with-superlu_dist-include=${SUPERLU_DIST_DIR}"
fi

# triangle
if [ -f "/usr/lib/libtriangle.so" ]; then
  CONFOPTS="${CONFOPTS} --with-triangle=1"
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
