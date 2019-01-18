# Maintainer: Alessandro G. Magnasco <alessandromagnasco at gmail dot com>
# Contributor: Bertrand Lacoste <bertrandlacoste at gmail dot com>
# Contributor: Tim Langlois <langlois at cs dot cornell dot edu>
# Maintainer: Christian Pfeiffer <cpfeiffer at live dot de>
# Contributor: Wink Saville <wink at saville dot com>

pkgname=hypre
pkgver=2.15.1
pkgrel=1
pkgdesc="A library for solving large, sparse linear systems on massively parallel computers"
arch=('x86_64')
url="http://acts.nersc.gov/hypre"
license=('lgpl')
depends=('superlu' 'superlu_dist')
makedepends=('gcc-fortran')
source=(https://github.com/LLNL/hypre/archive/v${pkgver}.tar.gz
        hypre-config-fix.patch)
sha512sums=('5be677727b815b2eb0cd711b65ff6b4ef798f42023ec2831e66bfbba7de0288208c67257734641b40f884868e8b0db97bb12d4d3ea27e97e36041eacc7ac9fa2'
            '280f1577b20ae13f94b5c98fc05836a6784285bdb34a2622230861b02b464793ce915a81378838c0a222fd8d4341c40ae658ca5ff2099ec10d08a67f8cfa150d')

prepare() {
  _build_dir="${srcdir}/${pkgname}-${pkgver}${_suffix}"
  cd "${_build_dir}"

  patch -p1 -i ../hypre-config-fix.patch
}

build() {
  _build_dir="${srcdir}/${pkgname}-${pkgver}${_suffix}"
  cd "${_build_dir}/src"
    
  # disable internal superlu and fei for now, not sure yet how to get it to use external superlu
  CFLAGS="${CFLAGS} -fopenmp" CXXFLAGS="${CXXFLAGS} -fopenmp" LDFLAGS="${LDFLAGS} -lgomp" \
  ./configure --prefix="${pkgdir}/usr" --enable-shared \
      --with-superlu --with-superlu-include=/usr/include/superlu --with-superlu-lib="-lsuperlu" \
      --with-dsuperlu --with-dsuperlu-include=/usr/include/superlu_dist --with-dsuperlu-lib="-lsuperlu_dist" \
      --with-fei --with-blas --with-lapack --with-openmp --enable-fortran --with-mli --with-MPI

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

