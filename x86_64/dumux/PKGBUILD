# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dumux
_dunever=2.10.0
_tarver=3.10.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=2
pkgdesc="An open-source simulator and research code in modern C++"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL-3.0-or-later)
depends=("dune-grid>=${_dunever}" "dune-istl>=${_dunever}" "dune-localfunctions>=${_dunever}")
makedepends=(doxygen graphviz python-scikit-build)
optdepends=('dune-alugrid: for grid manager ALUGrid support'
  'dune-foamgrid: for grid manager FoamGrids support'
  'dune-functions: for functions spaces support'
  'opm-grid: for cornerpoint grid support'
  'dune-subgrid: for grid manager SubGrid support'
  'dune-spgrid: for grid manager SPGrid support'
  'dune-mmesh: for grid manager MMesh support')
source=(https://git.iws.uni-stuttgart.de/${pkgname}-repositories/${pkgname}/-/archive/${_tar})
sha512sums=('4f285e359fc999949ec347390bcc6feb5c291d10e974a720d1f1468a771177d231240da6094c2fa3941adb799ccd097fc58376c20fc7d0fd9518fa21ef0f6f01')

prepare() {
  cd ${pkgname}-${pkgver}
  export _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  sed -i 's/^Version: '"${pkgver%%.0}"'/Version: '"${pkgver}"'/' dune.module
  sed -i "s/'requests',/'requests', 'dune-geometry',/" pyproject.toml
  sed -i 's/"python"/"\/usr\/include\/dumux\/common\/"/' python/dumux/common/properties.py
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
    -DENABLE_HEADERCHECK=ON \
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DDUNE_PYTHON_INSTALL_LOCATION='none' \
    -DDUNE_PYTHON_WHEELHOUSE="dist"
}

package() {
  cd ${pkgname}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py --skip-cmake install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  install -Dm 644 python/${pkgname}/__init__.py -t "${pkgdir}${site_packages}"/${pkgname}
  find "${pkgdir}" -type d -empty -delete
}
