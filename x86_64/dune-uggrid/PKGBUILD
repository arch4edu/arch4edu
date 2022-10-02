# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-uggrid
_tarver=2.8.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver=${_tarver}
pkgrel=1
pkgdesc="UG grid manager"
arch=('x86_64')
url="https://dune-project.org/modules/${pkgname}"
license=('LGPL')
depends=('dune-common>=2.8.0')
makedepends=('doxygen' 'graphviz')
optdepends=('doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('c3e82b753650e6ae41c91eb92934cacc4874f764ffa15a6077a71d160f6af0366b7e74f8929cf48f9672bd52ff89d85e41f2f6735cb026503693521b25eb7b51' 'SKIP')
validpgpkeys=('ABE52C516431013C5874107C3F71FE0770D47FFB') # Markus Blatt (applied mathematician and DUNE core developer) <markus@dr-blatt.de>

prepare() {
  sed -i 's/^add_subdirectory(lib)/#add_subdirectory(lib)/' "${pkgname}-${_tarver}/dune/uggrid/CMakeLists.txt"
}

build() {
  cmake \
    -S ${pkgname}-${_tarver} \
    -B build-cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
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
