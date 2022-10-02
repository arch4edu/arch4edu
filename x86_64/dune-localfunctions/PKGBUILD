# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgbase=dune-localfunctions
pkgname=(${pkgbase} python-${pkgbase})
_tarver=2.8.0
_tar="${_tarver}/${pkgbase}-${_tarver}.tar.gz"
pkgver=${_tarver}
pkgrel=2
pkgdesc="Local Finite Elements"
arch=('x86_64')
url="https://dune-project.org/modules/${pkgbase}"
license=('custom:GPL2 with runtime exception')
makedepends=('dune-geometry>=2.8.0' 'texlive-core' 'doxygen' 'graphviz' 'python-setuptools')
optdepends=('texlive-core: Type setting system'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('4faf58cc5d891d8cbd528ec0d337dc9b8b6c2c55189f8126c7a81ed323e3843193394a2b31b78fc56e80015356a195e25915855823408a7e985ebe17ab4c7b90' 'SKIP')
validpgpkeys=('ABE52C516431013C5874107C3F71FE0770D47FFB') # Markus Blatt (applied mathematician and DUNE core developer) <markus@dr-blatt.de>

prepare() {
  sed -i '5 a BUILD_ON_INSTALL' ${pkgbase}-${_tarver}/doc/CMakeLists.txt
}

build() {
  cmake \
    -S ${pkgbase}-${_tarver} \
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
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DDUNE_PYTHON_INSTALL_LOCATION='none' \
    -Wno-dev
  cmake --build build-cmake --target all
  cd "build-cmake/python"
  python setup.py build
}

package_dune-localfunctions() {
  depends=('dune-geometry>=2.8.0')
  DESTDIR="${pkgdir}" cmake --build build-cmake --target install
  install -m644 -D ${pkgbase}-${_tarver}/COPYING "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
  find "${pkgdir}" -type d -empty -delete
}

package_python-dune-localfunctions() {
  depends=('dune-localfunctions>=2.8.0' 'python-dune-common>=2.8.0')
  pkgdesc+=" (python bindings)"
  cd "build-cmake/python"
  export PYTHONHASHSEED=0
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
}
