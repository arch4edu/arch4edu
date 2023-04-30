# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dumux
_dunever=2.9.0
_tarver=3.7.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=2
pkgdesc="An open-source simulator and research code in modern C++"
arch=(x86_64)
url="https://${pkgname}.org"
license=(GPL3)
depends=("dune-grid>=${_dunever}" "dune-istl>=${_dunever}" "dune-localfunctions>=${_dunever}")
makedepends=(doxygen graphviz python-scikit-build python-ninja)
optdepends=('dune-alugrid: for grid manager ALUGrid support'
  'dune-foamgrid: for grid manager FoamGrids support'
  'dune-functions: for functions spaces support'
  'opm-grid: for cornerpoint grid support'
  'dune-subgrid: for grid manager SubGrid support'
  'dune-spgrid: for grid manager SPGrid support'
  'dune-mmesh: for grid manager MMesh support')
source=(https://git.iws.uni-stuttgart.de/${pkgname}-repositories/${pkgname}/-/archive/${_tar})
sha512sums=('b68a75d73700c4cda4b65450b0b2f0a63521e3211c36f01be0d8c2ef5406d810c30b939042bd76edb90ed76f8d38da0e07becc6c94990a5f9d14c0dce36abc2e')

prepare() {
  cd ${pkgname}-${pkgver}
  export _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  sed -i 's/^Version: '"${pkgver%%.0}"'/Version: '"${pkgver}"'/' dune.module
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
  mv "${pkgdir}"/usr/python/dune/data "${pkgdir}${site_packages}"/${pkgname}
  find "${pkgdir}" -type d -empty -delete
}
