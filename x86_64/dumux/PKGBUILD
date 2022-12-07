# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dumux
_dunever=2.9.0
_tarver=3.6.0
_tar="${_tarver}/${pkgname}-${_tarver}.tar.gz"
pkgver="${_tarver}"
pkgrel=2
pkgdesc="An open-source simulator and research code in modern C++"
arch=(x86_64)
url="https://${pkgname}.org"
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
sha512sums=('c47f478297865baddbf3a0770f92a035807f3b87e2ba4becbb03fcc08d073684973a621688c13750d3840fb34f83ad19a091018e5529382a1e049c68bee18d08')

prepare() {
  cd ${pkgname}-${pkgver}
  export _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")

  sed -i 's/#include <opm\/parser\/eclipse\/Parser\/Parser.hpp>/#include <opm\/input\/eclipse\/Parser\/Parser.hpp>/' dumux/io/grid/cpgridmanager.hh
  sed -i 's/#include <opm\/parser\/eclipse\/Parser\/ParseContext.hpp>/#include <opm\/input\/eclipse\/Parser\/ParseContext.hpp>/' dumux/io/grid/cpgridmanager.hh
  sed -i 's/#include <opm\/parser\/eclipse\/Deck\/Deck.hpp>/#include <opm\/input\/eclipse\/Deck\/Deck.hpp>/' dumux/io/grid/cpgridmanager.hh
  sed -i 's/#include <opm\/parser\/eclipse\/EclipseState\/EclipseState.hpp>/#include <opm\/input\/eclipse\/EclipseState\/EclipseState.hpp>/' dumux/io/grid/cpgridmanager.hh

  sed -i 's/#include <opm\/parser\/eclipse\/Deck\/Deck.hpp>/#include <opm\/input\/eclipse\/Deck\/Deck.hpp>/' test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/getKeyword("PORO").getRawDoubleData()/getKeywordList("PORO").back()->getRawDoubleData()/' test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/getKeyword("PERMX").getRawDoubleData()/getKeywordList("PERMX").back()->getRawDoubleData()/' test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/getKeyword("PERMZ").getRawDoubleData()/getKeywordList("PERMZ").back()->getRawDoubleData()/' test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/^Version: '"${pkgver%%.0}"'-git/Version: '"${pkgver}"'/' dune.module
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
    -DCMAKE_VERBOSE_MAKEFILE=ON \
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
  find "${pkgdir}" -type d -empty -delete
  cd "${pkgdir}"
  rm -r usr/python
}
