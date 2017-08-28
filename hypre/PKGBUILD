# Maintainer: Alessandro G. Magnasco <alessandromagnasco at gmail dot com>
# Contributor: Bertrand Lacoste <bertrandlacoste at gmail dot com>
# Contributor: Tim Langlois <langlois at cs dot cornell dot edu>
# Contributor: Wink Saville <wink at saville dot com>

pkgname=hypre
pkgver=2.11.2
_suffix=
pkgrel=1
pkgdesc="A library for solving large, sparse linear systems on massively parallel computers"
arch=('i686' 'x86_64')
url="http://acts.nersc.gov/hypre"
license=('lgpl')
depends=('gcc-libs' 'gcc-fortran' 'openmpi' 'blas' 'lapack' 'superlu')
source=(https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods/download/${pkgname}-${pkgver}.tar.gz)
md5sums=('d507943a1a3ce5681c3308e2f3a6dd34')

build() {
  _build_dir="${srcdir}/${pkgname}-${pkgver}${_suffix}"
  cd "${_build_dir}/src"
  

  CFLAGS='-O3 -fopenmp -DMPIPP_H'
  CXXFLAGS='-O3 -fopenmp -DMPIPP_H'
  MPI_FLAGS=(--with-MPI --with-openmp --with-MPI-lib-dirs=/usr/lib/openmpi)
  MPI_FLAGS+=(--with-MPI-libs="gomp mpi mpi_usempif08 mpi_usempi_ignore_tkr mpi_mpifh gfortran m quadmath pthread")
    
  # disable internal superlu and fei for now, not sure yet how to get it to use external superlu
  ./configure --prefix=/usr --enable-shared \
      --with-superlu --with-extra-incpath=/usr/include/superlu \
      --without-fei --without-babel \
      --with-blas=yes --with-lapack=yes \
      "${MPI_FLAGS[@]}" \
      CFLAGS="${CFLAGS}" CXXFLAGS="${CXXFLAGS}"
  make
}

check() {
  _build_dir="${srcdir}/${pkgname}-${pkgver}${_suffix}"
  cd "${_build_dir}/src"

  make test
}

package() {
  _build_dir="${srcdir}/${pkgname}-${pkgver}${_suffix}"
  cd "${_build_dir}/src"

  mkdir -p ${pkgdir}/usr/lib ${pkgdir}/usr/include

  install -m644 ${_build_dir}/src/hypre/include/*.h ${pkgdir}/usr/include
  install -m644 ${_build_dir}/src/hypre/lib/libHYPRE-${pkgver}.so ${pkgdir}/usr/lib
  ln -s libHYPRE-${pkgver}.so ${pkgdir}/usr/lib/libHYPRE.so
}

