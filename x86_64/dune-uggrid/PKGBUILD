# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-uggrid
_tarver=2.9.1
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=1
pkgdesc="UG grid manager"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=('LGPL')
depends=("dune-common>=${pkgver}")
makedepends=(doxygen graphviz)
optdepends=('doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('debad9b205ba4d721ec91ad6cc925bd9b31d7560cf42a0d17d5603e8e97d1d4aabe8674d8009f985a720053ac81d3c5954f2f393f043a00b154f74fb51d5b06c'
  'SKIP')
validpgpkeys=('2AA99AA4E2D6214E6EA01C9A4AF42916F6E5B1CF') # Christoph Grüninger <gruenich@dune-project.org>

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
    -DCMAKE_CXX_STANDARD=17 \
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
  find "${pkgdir}" -type d -empty -delete
}
