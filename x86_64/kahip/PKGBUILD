# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=KaHIP
pkgname=${_base,,}
pkgver=3.16
pkgrel=1
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=('x86_64')
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(openmpi openmp metis gperftools)
makedepends=(cmake)
optdepends=('gurobi: for ILP solver in ilp_improve')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('58f6865159250f2e70fcdd9aec87bf5f3c1e7574b599caca934dc11c4d3b7028ecdc6b802dd4a55ea33f827b1e6e012981f5bbc50c3e91fca6cdb5c237ded423')

build() {
  cmake \
    -S ${_base}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=11 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${_base}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
