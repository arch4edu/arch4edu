# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-istl
_tarver=2.10.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=1
pkgdesc="Iterative Solver Template Library"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=(LicenseRef-GPL-2.0-only-with-DUNE-exception)
depends=("dune-common>=${pkgver}" arpack)
makedepends=(texlive-latexextra biber doxygen graphviz python-scikit-build)
optdepends=('vc: C++ Vectorization library'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'parmetis: Parallel Graph Partitioning and Fill-reducing Matrix Ordering'
  'scotch: Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering'
  'superlu: Set of subroutines to solve a sparse linear system'
  'arpackpp: C++ interface to ARPACK'
  'suitesparse: A collection of sparse matrix libraries')
options=(!emptydirs)
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('067fc9a35704a63b7b1c81ca20893b3e47af69633db409d7faa1501a1a0f920bcf5b76c005ee29c65c2ebf0d05bced242313cefe93641cd262317c4e4cf9e5a3'
  'SKIP')
validpgpkeys=('703607A1FD9AF4205E735522B95BE0EFB19724A1') # Simon Praetorius <simon.praetorius@tu-dresden.de>

prepare() {
  cd ${pkgname}-${pkgver}
  # install header for run test/linear/test_linearsolver.cc in dumux
  sed -i '115 a install(FILES anisotropic.hh DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/dune/istl/paamg/test)' dune/istl/paamg/test/CMakeLists.txt
  sed -i '8 a BUILD_ON_INSTALL' doc/CMakeLists.txt
  # https://git.iws.uni-stuttgart.de/dumux-repositories/dumux/-/blob/master/patches/istl-2.6.patch
  sed -i 's/*coarseSmoother_, 1E-2, 1000, 0/*coarseSmoother_, 1E-12, 1000, 0/' dune/istl/paamg/amg.hh
  export _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  python -m venv --system-site-packages _skbuild/linux-${CARCH}-${_pyversion}/cmake-build/dune-env
}

build() {
  cd ${pkgname}-${pkgver}

  XDG_CACHE_HOME="${PWD}" \
    python setup.py build \
    --build-type=None \
    -G 'Unix Makefiles' \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_FLAGS='-Wall -fdiagnostics-color=always' \
    -DCMAKE_CXX_FLAGS="-O2 -Wall -fdiagnostics-color=always -mavx" \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DCMAKE_DISABLE_FIND_PACKAGE_LATEX=FALSE \
    -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=FALSE \
    -DCMAKE_DISABLE_FIND_PACKAGE_Vc=TRUE \
    -DENABLE_HEADERCHECK=ON \
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DDUNE_PYTHON_INSTALL_LOCATION='none' \
    -DDUNE_PYTHON_WHEELHOUSE="dist"
}

package() {
  cd ${pkgname}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py --skip-cmake install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
