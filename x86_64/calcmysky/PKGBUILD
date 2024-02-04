# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Frederik “Freso” S. Olesen <archlinux@freso.dk>
_base=CalcMySky
pkgname=${_base,,}
pkgver=0.3.1
pkgrel=2
pkgdesc="Simulator of light scattering by planetary atmospheres"
arch=(x86_64)
url="https://github.com/10110111/${_base}"
license=(GPL-3.0-or-later)
depends=(eigen glm qt6-base)
makedepends=(cmake ninja)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  glm.patch::${url}/pull/18.patch)
sha512sums=('3038feffdf3a61d49d39304b72f1c2809ea5e3a835c4b3c1603162802afc3d27af6cdfd63eb3286e9e614850b73e338e1cc2cf6a6e915ea968194c0a7a9a56eb'
  '354ada3efc2b6ac5ab3213c56f01209ae06c49729be57229fa008b8093dbbff00654cde7d8320255a880849c715dfa2013b232747fc36d8827f1f2dbb3445dad')

prepare() {
  cd ${_base}-${pkgver}
  patch -p1 -i ../glm.patch
}

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
