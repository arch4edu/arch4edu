# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Frederik “Freso” S. Olesen <archlinux@freso.dk>
_base=CalcMySky
pkgname=${_base,,}
pkgver=0.3.2
pkgrel=1
pkgdesc="Simulator of light scattering by planetary atmospheres"
arch=(x86_64)
url="https://github.com/10110111/${_base}"
license=(GPL-3.0-or-later)
depends=(eigen glm qt6-base)
makedepends=(cmake ninja)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('a7f69b25c54be86ce179a118ca8a6d606e2c0fe7dc238b46620237e311dc5198a2aeb70e4885cc6553a26f7c38b78b5a338115a4606161fa249a806e891f88b6')

build() {
  cmake \
    -S ${_base}-${pkgver} \
    -B build \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_CXX_FLAGS="-fPIC" \
    -DQT_VERSION=6 \
    -Wno-dev
  cmake --build build --target all
}

check() {
  cmake --build build --target test
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${_base}-${pkgver}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
