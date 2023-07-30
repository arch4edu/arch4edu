# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Jed Brown <jed@jedbrown.org>
# Contributor: George Eleftheriou <eleftg@gmail.com>
# Contributor: mickele
# Contributor: gborzi
# Contributor: abenson
_base=METIS
pkgname=${_base,,}
pkgver=5.2.1
pkgrel=1
arch=(x86_64)
pkgdesc="Serial Graph Partitioning and Fill-reducing Matrix Ordering"
url="https://github.com/KarypisLab/${_base}"
license=(Apache)
depends=(glibc gklib)
makedepends=(cmake)
options=(docs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('69127b7a777f9ba14cf399a7122000af9d6094a5f44be600a28384cfc0495c024fb0c6eab37c4473a5763ec1077cd9f30d9bcbb3c952462f6c9ead31c6b9e790')

build() {
  cd ${_base}-${pkgver}
  make config \
    i64=0 \
    r64=0 \
    gdb=0 \
    assert=0 \
    assert2=0 \
    debug=0 \
    gprof=0 \
    valgrind=0 \
    openmp=0 \
    shared=1 \
    cc=gcc \
    prefix=/usr \
    gklib_path=/usr
}

package() {
  cd ${_base}-${pkgver}
  make install DESTDIR="${pkgdir}"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
