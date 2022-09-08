# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=KaHIP
pkgname=${_base,,}
pkgver=3.14
pkgrel=1
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=('x86_64')
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(openmpi openmp metis gperftools)
makedepends=(cmake)
optdepends=('gurobi: for ILP solver in ilp_improve')
source=(${url}/archive/v${pkgver}.tar.gz)
sha512sums=('23cf77f6cdd4f93b33e9ae614e953bb74946b5efaaa5849190257ec92ef91b131e7515c0a856a06aa94e8dd80e290e4395541058808e7309ca4c67b9ec53f64c')

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
