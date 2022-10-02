# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgbase=dune-istl
pkgname=(${pkgbase} python-${pkgbase})
_tarver=2.8.0
_tar="${_tarver}/${pkgbase}-${_tarver}.tar.gz"
pkgver=${_tarver}
pkgrel=2
pkgdesc="Iterative Solver Template Library"
arch=('x86_64')
url="https://dune-project.org/modules/${pkgbase}"
license=('custom:GPL2 with runtime exception')
makedepends=('dune-common>=2.8.0' 'texlive-latexextra' 'biber' 'doxygen' 'graphviz' 'python-setuptools')
optdepends=('vc: C++ Vectorization library'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'parmetis: Parallel Graph Partitioning and Fill-reducing Matrix Ordering'
  'scotch: Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering'
  'superlu: Set of subroutines to solve a sparse linear system'
  'arpackpp: C++ interface to ARPACK'
  'suitesparse: A collection of sparse matrix libraries')
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('03139c71881bc83934a1468937196e77c42deaba776102f49309ee1e46163ff44263524733d2522a1d912bcfdf6de3ba792834f2435cfa6d01670a52a8b80289' 'SKIP')
validpgpkeys=('ABE52C516431013C5874107C3F71FE0770D47FFB') # Markus Blatt (applied mathematician and DUNE core developer) <markus@dr-blatt.de>

prepare() {
  # install header for run test/linear/test_linearsolver.cc in DuMuX
  sed -i '123 a install(FILES anisotropic.hh DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/dune/istl/paamg/test)' ${pkgbase}-${_tarver}/dune/istl/paamg/test/CMakeLists.txt
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
    -DCMAKE_DISABLE_FIND_PACKAGE_Vc=TRUE \
    -Wno-dev
  cmake --build build-cmake --target all
  cd "build-cmake/python"
  python setup.py build
}

package_dune-istl() {
  depends=('dune-common>=2.8.0')
  DESTDIR="${pkgdir}" cmake --build build-cmake --target install
  install -Dm644 ${pkgbase}-${_tarver}/COPYING "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
  find "${pkgdir}" -type d -empty -delete
}

package_python-dune-istl() {
  depends=('dune-istl>=2.8.0' 'python-dune-common>=2.8.0' 'arpack')
  pkgdesc+=" (python bindings)"
  cd "build-cmake/python"
  export PYTHONHASHSEED=0
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
}
