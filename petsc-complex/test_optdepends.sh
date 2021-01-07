#!/bin/bash

# Test if external packages for PETSC are installed

CONFOPTS=""

## External downloads
#for external_pkg in hypre; do
	#CONFOPTS="${CONFOPTS} --download-${external_pkg}=1"
#done

# Add hypre support
if [ -f "/usr/lib/libHYPRE.so" ]; then
  VERSION_MIN=2.14.0
  VERSION=$(readlink -f '/usr/lib/libHYPRE.so' | sed -r 's/^.*libHYPRE-(.*)\.so/\1/')

	if [ "$VERSION_MIN" = "$(printf '%s\n' "$VERSION_MIN" "$VERSION" | sort -V | head -n1)" ]; then
		CONFOPTS="${CONFOPTS} --with-hypre-lib=/usr/lib/libHYPRE.so --with-hypre-include=/usr/include/hypre"
	else
		(>&2 echo "WARNING: COMPILING PETSc WITHOUT HYPRE.")
		(>&2 echo "HYPRE $VERSION FOUND BUT AT LEAST $VERSION_MIN IS REQUIRED.")
	fi
fi

# Add mumps support
if [ -f "/usr/lib/libmumps_common.so" ]; then
	CONFOPTS="${CONFOPTS} --with-mumps=1"
fi

# Add fftw support
if [ -f "/usr/lib/libfftw3_mpi.so" ]; then
	CONFOPTS="${CONFOPTS} --with-fftw=1"
fi

# Add triangle support
if [ -f "/usr/lib/libtriangle.so" ]; then
	CONFOPTS="${CONFOPTS} --with-triangle=1"
fi

# Add hdf5 support
if [[ "$(h5stat -V)" ]]; then
	CONFOPTS="${CONFOPTS} --with-hdf5=1"
fi

# Add scalapack support
if [ -f "/usr/lib/pkgconfig/scalapack.pc" ]; then
	CONFOPTS="${CONFOPTS} --with-scalapack=1"
fi

# Add suitesparse support
if [ -f "/usr/include/SuiteSparse_config.h" ]; then
	CONFOPTS="${CONFOPTS} --with-suitesparse=1"
fi

# Add metis support
if [ -f "/usr/include/metis.h" ]; then
	CONFOPTS="${CONFOPTS} --with-metis=1"
	# Add parmetis support
	if [ -f "/usr/include/parmetis.h" ]; then
		CONFOPTS="${CONFOPTS} --with-parmetis=1"
	fi
fi

# Add scotch support
SCOTCH_DIR="/usr/include/scotch"
if [ -d "${SCOTCH_DIR}" ]; then
	SCOTCH_LIBS="libesmumps.so,libptscotch.so,libptscotcherr.so,libscotch.so,libscotcherr.so"
	# Include bzip2 if scotch was build with bzip2 support
	if [ -f /usr/include/bzlib.h ];then
		SCOTCH_LIBS="${SCOTCH_LIBS},libbz2.so"
	fi
	SCOTCH_LIBS="[${SCOTCH_LIBS}]"
	CONFOPTS="${CONFOPTS} --with-ptscotch=1 --with-ptscotch-lib=${SCOTCH_LIBS} --with-ptscotch-include=${SCOTCH_DIR}"
fi

# Add superlu support
SUPERLU_DIR="/usr/include/superlu"
if [ -d "${SUPERLU_DIR}" ]; then
	CONFOPTS="${CONFOPTS} --with-superlu=1 --with-superlu-lib=-lsuperlu --with-superlu-include=${SUPERLU_DIR}"
fi

# Add superlu_dist support
SUPERLU_DIST_DIR="/usr/include/superlu_dist"
if [ -d "${SUPERLU_DIST_DIR}" ]; then
	CONFOPTS="${CONFOPTS} --with-superlu_dist=1 --with-superlu_dist-lib=-lsuperlu_dist --with-superlu_dist-include=${SUPERLU_DIST_DIR}"
fi

# Add pastix support
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

# Add trilinos support
#if [ -f "/usr/lib/libml.so" ]; then
#	CONFOPTS="${CONFOPTS} --with-ml=1"
#	# Add boost support (may be useful for trilinos)
#	CONFOPTS="${CONFOPTS} --with-boost=1"
#fi

echo "${CONFOPTS}"
