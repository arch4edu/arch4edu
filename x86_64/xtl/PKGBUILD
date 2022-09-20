# Maintainer: Simon Wilper <sxw@chronowerks.de>
pkgname=xtl
pkgver=0.7.4
pkgrel=1
pkgdesc="The x template library"
arch=('any')
url="https://github.com/xtensor-stack/${pkgname}"
license=('BSD-3-Clause')
depends=('gcc')
makedepends=('cmake')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")

build() {
  cmake -B "${pkgname}-${pkgver}/build" -S "${pkgname}-${pkgver}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib
  make -C "${pkgname}-${pkgver}/build"
}

package() {
  cd ${pkgname}-${pkgver}
  make -C build DESTDIR="${pkgdir}" install
}
sha512sums=('8da3f95048cb701222799e23d1934139d9cbc70edd4547315a27e3f1ec853987290da3a4295411e51785d30237d9dbbe9afc0deed24a8a77da78167940a0e641')
