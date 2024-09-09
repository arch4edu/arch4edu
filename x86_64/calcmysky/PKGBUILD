# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Frederik “Freso” S. Olesen <archlinux@freso.dk>
_base=CalcMySky
pkgname=${_base,,}
pkgver=0.3.3
pkgrel=1
pkgdesc="Simulator of light scattering by planetary atmospheres"
arch=(x86_64)
url="https://github.com/10110111/${_base}"
license=(GPL-3.0-or-later)
depends=(eigen glm qt6-base)
makedepends=(cmake ninja)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('186281ad2aafac7006117cfb65d91c8053ab3caa9d4f67e5463471538bae40fd8fcc954c3fe9b9d2ca7bba4e6a1fdf8de33980469930cc23b1c21ee4b333917e')

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
