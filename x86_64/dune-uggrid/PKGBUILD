# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-uggrid
_tarver=2.10.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=1
pkgdesc="UG grid manager"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=(LGPL-2.1-or-later)
depends=("dune-common>=${pkgver}")
makedepends=(doxygen graphviz)
optdepends=('doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software')
options=(!emptydirs)
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('e28cb28bf73a20fa765eb1e76643a1f38fba30fffca8865fcf33fa950f1b43f577eeadfa19eea6fc5773233500e280e839fc8cc140715159add359ab4cddcf23'
  'SKIP')
validpgpkeys=('703607A1FD9AF4205E735522B95BE0EFB19724A1') # Simon Praetorius <simon.praetorius@tu-dresden.de>

prepare() {
  sed -i 's/^add_subdirectory(lib)/#add_subdirectory(lib)/' ${pkgname}-${_tarver}/dune/uggrid/CMakeLists.txt
}

build() {
  cmake \
    -S ${pkgname}-${_tarver} \
    -B build-cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_FLAGS='-Wall -fdiagnostics-color=always' \
    -DCMAKE_CXX_FLAGS="-Wall -fdiagnostics-color=always -mavx" \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DENABLE_HEADERCHECK=ON \
    -Wno-dev
  cmake --build build-cmake --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build-cmake --target install
  install -Dm644 ${pkgname}-${_tarver}/COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
