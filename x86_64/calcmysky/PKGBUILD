# Maintainer: Carlos Aznarán <caznaranl@uni.pe>

_base=CalcMySky
pkgname=${_base,,}
pkgver=0.3.0
pkgrel=1
pkgdesc="Simulator of light scattering by planetary atmospheres"
arch=(x86_64)
url="https://github.com/10110111/${_base}"
license=(GPL)
depends=('eigen' 'glm' 'qt6-base')
makedepends=('cmake' 'ninja')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('529e9cd3d1e71e5ba3e910e9af44e5ddf1af105b499948325401faa9e0cf7911d8ef003570f5bb5395ff6954c37ae6fd7242eb1300f78636232d745012d495ef')

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
  find "${pkgdir}" -type d -empty -delete
}
