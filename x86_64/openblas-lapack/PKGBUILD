# Maintainer: thrasibule <guillaume.horel@gmail.com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Jiaxi Hu <sftrytry _AT_ gmail _DOT_ com>
# Contributor: Giuseppe Borzi <gborzi _AT_ ieee _DOT_ org>

pkgname=openblas-lapack
_PkgName=OpenBLAS
_pkgname=openblas
pkgver=0.3.22
# grep VERSION "${srcdir}/${_PkgName}-${pkgver}"/lapack-netlib/README.md | tail -n 1 | cut -d ' ' -f 2
_lapackver=3.11.0
_blasver=3.11.0
pkgrel=2
pkgdesc="Optimized BLAS library based on GotoBLAS2 1.13 BSD (providing blas, lapack, and cblas)"
arch=('x86_64')
url="http://www.openblas.net/"
license=('BSD')
depends=('gcc-libs')
makedepends=('perl' 'gcc-fortran')
provides=('openblas' "blas=${_blasver}" "lapack=${_lapackver}" "cblas=${_blasver}" "lapacke=${_lapackver}")
conflicts=('openblas' 'blas' 'lapack' 'cblas' 'lapacke')
options=(!emptydirs)
source=(${_PkgName}-${pkgver}.tar.gz::https://github.com/xianyi/OpenBLAS/releases/download/v${pkgver}/OpenBLAS-$pkgver.tar.gz)
sha256sums=('7fa9685926ba4f27cfe513adbf9af64d6b6b63f9dcabb37baefad6a65ff347a7')

# Add the following line to the _config variable if you want to set the number of make jobs
#  MAKE_NB_JOBS=2 \
_config="FC=gfortran USE_OPENMP=1 USE_THREAD=1 \
  USE_TLS=1 \
  MAJOR_VERSION=${_lapackver:0:1} NO_STATIC=1"

build(){
  cd "${_PkgName}-${pkgver}"
  unset MAKEFLAGS
  make ${_config} shared
}

package(){
  cd "${_PkgName}-${pkgver}"

  make ${_config} PREFIX=/usr DESTDIR="${pkgdir}" install

  # Install license
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Symlink to provide blas, cblas, lapack and lapacke
  cd "${pkgdir}/usr/lib/"
  # BLAS
  ln -sf libopenblas.so libblas.so
  ln -sf libopenblas.so libblas.so.${_blasver:0:1}
  ln -sf libopenblas.so libblas.so.${_blasver}
  # CBLAS
  ln -sf libopenblas.so libcblas.so
  ln -sf libopenblas.so libcblas.so.${_blasver:0:1}
  ln -sf libopenblas.so libcblas.so.${_blasver}
  # LAPACK
  ln -sf libopenblas.so liblapack.so
  ln -sf libopenblas.so liblapack.so.${_lapackver:0:1}
  ln -sf libopenblas.so liblapack.so.${_lapackver}
  # LAPACKE
  ln -sf libopenblas.so liblapacke.so
  ln -sf libopenblas.so liblapacke.so.${_lapackver:0:1}
  ln -sf libopenblas.so liblapacke.so.${_lapackver}
}
# vim:set ts=2 sw=2 et:
