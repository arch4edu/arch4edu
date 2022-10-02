# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgbase=dune-grid
pkgname=(${pkgbase} python-${pkgbase})
_tarver=2.8.0
_tar="${_tarver}/${pkgbase}-${_tarver}.tar.gz"
pkgver=${_tarver}
pkgrel=2
pkgdesc="Grid Interface and Implementations"
arch=('x86_64')
url="https://dune-project.org/modules/${pkgbase}"
license=('custom:GPL2 with runtime exception')
makedepends=('dune-geometry>=2.8.0' 'dune-uggrid>=2.8.0' 'doxygen' 'graphviz' 'python-setuptools')
optdepends=('doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'parmetis: Parallel Graph Partitioning and Fill-reducing Matrix Ordering'
  'psurface: Piecewise linear bijections between triangulated surfaces'
  'gnuplot: for provides gnuplot output for 1D and 2D Grids')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('534c77e5e930a960486945f23d2bb991dd5509aa077192a100e9060966c6ecf4eb977716164a4ae0042b3a77d3713f1079e5ee74666bc4e52b0037bcaac3723e' 'SKIP')
validpgpkeys=('ABE52C516431013C5874107C3F71FE0770D47FFB') # Markus Blatt (applied mathematician and DUNE core developer) <markus@dr-blatt.de>

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
    -DCMAKE_DISABLE_FIND_PACKAGE_Alberta=TRUE \
    -Wno-dev
  cmake --build build-cmake --target all
  cd "build-cmake/python"
  python setup.py build
}

package_dune-grid() {
  depends=('dune-geometry>=2.8.0' 'dune-uggrid>=2.8.0')
  DESTDIR="${pkgdir}" cmake --build build-cmake --target install
  install -Dm644 ${pkgbase}-${_tarver}/COPYING "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
  cd "${pkgdir}"
  rm -rf usr/python
  find "${pkgdir}" -type d -empty -delete
}

package_python-dune-grid() {
  depends=('dune-grid>=2.8.0' 'python-dune-geometry>=2.8.0')
  pkgdesc+=" (python bindings)"
  cd "build-cmake/python"
  export PYTHONHASHSEED=0
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
}
