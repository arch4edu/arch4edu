# Maintainer: Carlos Aznarán <caznaranl@uni.pe>

_base=CalcMySky
pkgname=${_base,,}
pkgver=0.2.1
pkgrel=1
pkgdesc="Simulator of light scattering by planetary atmospheres"
arch=(x86_64)
url="https://github.com/10110111/${_base}"
license=(GPL)
depends=('eigen' 'glm' 'qt6-base')
makedepends=('cmake' 'ninja')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('3915b965ee656b259ce7f158dfdd3c9c11a6c3ff907307899ae55e88ad6c1ccfbec8e0a1f784f5232fb0cb2c8300422fa25b8b1d4d11639d3ebb8c76d67059e5')

build() {
  cmake \
    -S ${_base}-${pkgver} \
    -B build \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_CXX_COMPILER=g++ \
    -DQT_VERSION=6 \
    -Wno-dev
  cmake --build build --target all
}

check() {
  cmake --build build --target test
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  find "${pkgdir}" -type d -empty -delete
}
