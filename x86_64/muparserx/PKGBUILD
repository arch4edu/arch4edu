# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Christian Pfeiffer <cpfeiffer at live dot de>
pkgname=muparserx
pkgver=4.0.12
pkgrel=1
pkgdesc="A fast math parser library with support for arrays, matrices and complex numbers"
arch=('x86_64')
url="https://github.com/beltoforion/${pkgname}"
license=('custom:BSD-2-clause')
makedepends=(cmake)
depends=(gcc-libs)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('5be7d846105c2eae7f9a7929147ff6890496ca80348c1b08c62fdf199a6b33d48225c4aeec00e03283e233c91574943b60ee4282169715f5ded8aa18fd9a732d')

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
