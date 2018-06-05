# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Jiaxi Hu <sftrytry _AT_ gmail _DOT_ com>
# Contributor: Giuseppe Borzi <gborzi _AT_ ieee _DOT_ org>

pkgname=openblas-lapack
_PkgName=OpenBLAS
_pkgname=openblas
pkgver=0.3.0
# grep VERSION "${srcdir}/${_PkgName}-${pkgver}"/lapack-netlib/README.md | tail -n 1 | cut -d ' ' -f 2
_lapackver=3.8.0
pkgrel=1
pkgdesc="Optimized BLAS library based on GotoBLAS2 1.13 BSD (providing blas, lapack, and cblas)"
arch=('any')
url="http://www.openblas.net/"
license=('BSD')
depends=('gcc-libs')
makedepends=('perl' 'gcc-fortran')
provides=('openblas' "blas=${_lapackver}" "lapack=${_lapackver}" "cblas=${_lapackver}" "lapacke=${_lapackver}")
conflicts=('openblas' 'blas' 'lapack' 'cblas' 'lapacke')
options=(!emptydirs)
source=(${_PkgName}-${pkgver}.tar.gz::https://github.com/xianyi/${_PkgName}/archive/v${pkgver}.tar.gz)
sha256sums=('cf51543709abe364d8ecfb5c09a2b533d2b725ea1a66f203509b21a8e9d8f1a1')

# Add the following line to the _config variable if you want to set the number of make jobs
#  MAKE_NB_JOBS=2 \
_config="FC=gfortran USE_OPENMP=0 USE_THREAD=1 \
  NO_LAPACK=0 BUILD_LAPACK_DEPRECATED=1"

build(){
  cd "${srcdir}/${_PkgName}-${pkgver}"

  make ${_config} libs netlib shared
}

check(){
  cd "${srcdir}/${_PkgName}-${pkgver}"

  make ${_config} tests
}

package(){
  cd "${srcdir}/${_PkgName}-${pkgver}"

  make ${_config} PREFIX=/usr DESTDIR="${pkgdir}" install

  # Install license
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Symlink to provide blas, cblas, lapack and lapacke
  cd "${pkgdir}/usr/lib/"
  # BLAS
  ln -sf libopenblas.so libblas.so
  ln -sf libopenblas.so libblas.so.${_lapackver:0:1}
  ln -sf libopenblas.so libblas.so.${_lapackver}
  # CBLAS
  ln -sf libopenblas.so libcblas.so
  ln -sf libopenblas.so libcblas.so.${_lapackver:0:1}
  ln -sf libopenblas.so libcblas.so.${_lapackver}
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
