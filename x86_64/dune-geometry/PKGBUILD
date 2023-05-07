# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-geometry
_tarver=2.9.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=2
pkgdesc="Geometry Transformations, Reference Elements and Quadrature Rules"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=('custom:GPL2 with runtime exception')
depends=("dune-common>=${pkgver}")
makedepends=(texlive-latexextra doxygen graphviz inkscape python-scikit-build python-ninja)
optdepends=('texlive-latexextra: Type setting system'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'inkscape: converts SVG images')
# 'python-quadpy: for quadrature rules'
source=(https://dune-project.org/download/${_tar}{,.asc}
  gcc13-compatibility.patch::https://gitlab.dune-project.org/core/${pkgname}/-/commit/3df3cb68b6b2c1b28d29c0353e42a63ab54768d1.patch)
sha512sums=('5b227b3346b7eb3db3887483525a3ce550eddfa13528c30b213a7cc811dead5844bf0032133d2167bd6f341be8b13c014cc208724e67cac074432af28cd39fb1'
  'SKIP'
  '047d6d7a8ba673d0f5ae22d2afc779e61f64727f9bd4e6a510515cb6e50572c3523b5aac0355b4ed867a684b8ca62e51d46947d637525e2c93e8b7d1ab3b60d0')
validpgpkeys=('E5B47782DE09813BCC3518E159DA94F1FC8FD313') # Andreas Dedner <a.s.dedner@warwick.ac.uk>

prepare() {
  cd ${pkgname}-${pkgver}
  export _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  sed -i 's/^Version: '"${pkgver%%.0}"'-git/Version: '"${pkgver}"'/' dune.module
  sed -i '7 a   BUILD_ON_INSTALL' doc/refinement/CMakeLists.txt
  # https://gitlab.dune-project.org/core/dune-geometry/-/merge_requests/217
  patch -p1 -i ../gcc13-compatibility.patch
  python -m venv --system-site-packages _skbuild/linux-${CARCH}-${_pyversion}/cmake-build/dune-env
}

build() {
  cd ${pkgname}-${pkgver}

  XDG_CACHE_HOME="${PWD}" \
    python setup.py build \
    --build-type=None \
    -G 'Unix Makefiles' \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_FLAGS='-Wall -fdiagnostics-color=always' \
    -DCMAKE_CXX_FLAGS="-O2 -Wall -fdiagnostics-color=always -mavx" \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DALLOW_CXXFLAGS_OVERWRITE=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_LATEX=FALSE \
    -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=FALSE \
    -DINKSCAPE=TRUE \
    -DENABLE_HEADERCHECK=ON \
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DDUNE_PYTHON_INSTALL_LOCATION='none' \
    -DDUNE_PYTHON_WHEELHOUSE="dist" \
    -DCMAKE_DISABLE_FIND_PACKAGE_Vc=TRUE
}

package() {
  cd ${pkgname}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py --skip-cmake install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
