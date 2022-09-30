# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Christian Pfeiffer <cpfeiffer at live dot de>
pkgname=muparserx
pkgver=4.0.11
pkgrel=1
pkgdesc="A fast math parser library with support for arrays, matrices and complex numbers"
arch=('x86_64')
url="https://github.com/beltoforion/${pkgname}"
license=('BSD')
makedepends=(cmake)
depends=(gcc-libs)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('67846a91b57e41731a656cfee68effdd9166e738108764be5d3080854d8a01bedbeacaaade7bee11c6b5f83019abddeca3b2c9acdfbb48629da6d9b92c79c7af')

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_EXAMPLES=OFF \
    -DCMAKE_SKIP_RPATH=ON \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
