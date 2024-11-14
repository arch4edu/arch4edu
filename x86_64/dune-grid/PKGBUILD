# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-grid
_tarver=2.10.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=2
pkgdesc="Grid Interface and Implementations"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=(LicenseRef-GPL-2.0-only-with-DUNE-exception)
depends=("dune-geometry>=${pkgver}" "dune-uggrid>=${pkgver}" alberta)
makedepends=(doxygen graphviz python-scikit-build)
optdepends=('imagemagick: image viewing/manipulation program'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'gnuplot: for provides gnuplot output for 1D and 2D Grids'
  'parmetis: Parallel Graph Partitioning and Fill-reducing Matrix Ordering')
options=(!emptydirs)
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('15eafca279fd9e1f11ae4c61effae74b3b1eedc976762cb0b5970cf1105d6c3c71039bb85b1cd00e846f8730133a2a9d0868e8961fc95c9f7c7ac2860e7fd46f'
  'SKIP')
validpgpkeys=('703607A1FD9AF4205E735522B95BE0EFB19724A1') # Simon Praetorius <simon.praetorius@tu-dresden.de>

prepare() {
  cd ${pkgname}-${pkgver}
  #   CMake Error at /usr/lib/cmake/dune-geometry/dune-geometry-config.cmake:18 (message):
  #   File or directory /usr/share/doc/dune-grid/grids/ referenced by variable
  #   DUNE_GRID_EXAMPLE_GRIDS_PATH does not exist !
  # Call Stack (most recent call first):
  #   /usr/lib/cmake/dune-grid/dune-grid-config.cmake:78 (set_and_check)
  #   /usr/share/dune/cmake/modules/DuneModuleDependencies.cmake:258 (find_package)
  #   /usr/share/dune/cmake/modules/DuneProject.cmake:114 (find_dune_package)
  #   CMakeLists.txt:22 (dune_project)
  sed -i '/set(DUNE_CUSTOM_PKG_CONFIG_SECTION/,+6 s/^/#/' CMakeLists.txt
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
    -DCMAKE_DISABLE_FIND_PACKAGE_Alberta=FALSE \
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
