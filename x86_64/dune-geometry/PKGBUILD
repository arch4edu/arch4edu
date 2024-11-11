# Maintainer: Josh Hoffer < hoffer dot joshua at gmail dot com >
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Lukas Böger <dev___AT___lboeger___DOT___de>
pkgname=dune-geometry
_tarver=2.10.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=1
pkgdesc="Geometry Transformations, Reference Elements and Quadrature Rules"
arch=(x86_64)
url="https://dune-project.org/modules/${pkgname}"
license=(LicenseRef-GPL-2.0-only-with-DUNE-exception)
depends=("dune-common>=${pkgver}")
makedepends=(texlive-latexextra doxygen graphviz inkscape python-scikit-build)
optdepends=('texlive-latexextra: Type setting system'
  'doxygen: Generate the class documentation from C++ sources'
  'graphviz: Graph visualization software'
  'inkscape: converts SVG images')
options=(!emptydirs)
source=(https://dune-project.org/download/${_tar}{,.asc})
sha512sums=('13ae5ef1e769082a4def16539d4c3f435d6a11be74e20ecdc898ca9b7285d980df94e9adfb9fe6a847c3245786aa9be1b3146fec91596f5200b340c1e151ed03'
  'SKIP')
validpgpkeys=('703607A1FD9AF4205E735522B95BE0EFB19724A1') # Simon Praetorius <simon.praetorius@tu-dresden.de>

prepare() {
  cd ${pkgname}-${pkgver}
  sed -i '7 a   BUILD_ON_INSTALL' doc/refinement/CMakeLists.txt
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
}
