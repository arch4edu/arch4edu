# Maintainer: Alessandro G. Magnasco <alessandromagnasco at gmail dot com>
# Contributor: Bertrand Lacoste <bertrandlacoste at gmail dot com>
# Contributor: Tim Langlois <langlois at cs dot cornell dot edu>
# Maintainer: Christian Pfeiffer <cpfeiffer at live dot de>
# Contributor: Wink Saville <wink at saville dot com>

pkgname=hypre
pkgver=2.18.2
pkgrel=1
pkgdesc="A library for solving large, sparse linear systems on massively parallel computers"
arch=('x86_64')
url="https://github.com/hypre-space/hypre"
license=('lgpl')
depends=('superlu' 'superlu_dist' 'openmpi')
makedepends=('gcc-fortran')
source=(https://github.com/hypre-space/hypre/archive/v${pkgver}.tar.gz)
sha512sums=('7b343a5c8530d7f5e31cad6c940c2f154b2b954566d4fe8525d690fec41db23936a46fb642a994791de32984e696c624804fb1fde1f0c9ce026f1a6e46b9c0f4')

build() {
  _build_dir="${srcdir}/${pkgname}-${pkgver}${_suffix}"
  cd "${_build_dir}/src"

  # disable internal superlu and fei for now, not sure yet how to get it to use external superlu
  CFLAGS="${CFLAGS} -fopenmp" CXXFLAGS="${CXXFLAGS} -fopenmp" LDFLAGS="${LDFLAGS} -lgomp" \
  ./configure --prefix="${pkgdir}/usr" --includedir="${pkgdir}/usr/include/hypre" --enable-shared \
      --with-superlu --with-superlu-include=/usr/include/superlu --with-superlu-lib="-lsuperlu" \
      --with-dsuperlu --with-dsuperlu-include=/usr/include/superlu_dist --with-dsuperlu-lib="-lsuperlu_dist" \
      --with-blas --with-lapack --with-openmp --enable-fortran --with-mli --with-MPI

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

  make install
}
