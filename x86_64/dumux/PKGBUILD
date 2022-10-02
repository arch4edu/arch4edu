# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgbase=dumux
pkgname=(${pkgbase} python-${pkgbase})
pkgver=3.5.0
_tar="${pkgver}/${pkgbase}-${pkgver}.tar.gz"
pkgrel=1
pkgdesc="An open-source simulator and research code in modern C++"
arch=(x86_64)
url="https://${pkgbase}.org"
license=(GPL3)
_dunever=2.8.0
makedepends=("dune-grid>=${_dunever}" "dune-istl>=${_dunever}" "dune-localfunctions>=${_dunever}" doxygen graphviz python-setuptools)
optdepends=('dune-alugrid'
  'dune-foamgrid: for grid manager FoamGrids support'
  'dune-functions: for functions spaces support'
  'opm-grid: for cornerpoint grid support'
  'dune-subgrid: for grid manager SubGrid support'
  'dune-spgrid: for grid manager SPGrid support'
  'dune-mmesh: for grid manager MMesh support')
source=(https://git.iws.uni-stuttgart.de/${pkgbase}-repositories/${pkgbase}/-/archive/${_tar})
sha512sums=('62d897340b6de634664f8a7db93ea26b777243643cb1f3c1f249323cf8f596e3964aec4c20f160333bd1b0dfb9291194c07f5237308dfea81f76f6d83dc5d4f7')

prepare() {
  sed -i 's/#include <opm\/parser\/eclipse\/Parser\/Parser.hpp>/#include <opm\/input\/eclipse\/Parser\/Parser.hpp>/' ${pkgbase}-${pkgver}/dumux/io/grid/cpgridmanager.hh
  sed -i 's/#include <opm\/parser\/eclipse\/Parser\/ParseContext.hpp>/#include <opm\/input\/eclipse\/Parser\/ParseContext.hpp>/' ${pkgbase}-${pkgver}/dumux/io/grid/cpgridmanager.hh
  sed -i 's/#include <opm\/parser\/eclipse\/Deck\/Deck.hpp>/#include <opm\/input\/eclipse\/Deck\/Deck.hpp>/' ${pkgbase}-${pkgver}/dumux/io/grid/cpgridmanager.hh
  sed -i 's/#include <opm\/parser\/eclipse\/EclipseState\/EclipseState.hpp>/#include <opm\/input\/eclipse\/EclipseState\/EclipseState.hpp>/' ${pkgbase}-${pkgver}/dumux/io/grid/cpgridmanager.hh

  sed -i 's/#include <opm\/parser\/eclipse\/Deck\/Deck.hpp>/#include <opm\/input\/eclipse\/Deck\/Deck.hpp>/' ${pkgbase}-${pkgver}/test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/getKeyword("PORO").getRawDoubleData()/getKeywordList("PORO").back()->getRawDoubleData()/' ${pkgbase}-${pkgver}/test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/getKeyword("PERMX").getRawDoubleData()/getKeywordList("PERMX").back()->getRawDoubleData()/' ${pkgbase}-${pkgver}/test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/getKeyword("PERMZ").getRawDoubleData()/getKeywordList("PERMZ").back()->getRawDoubleData()/' ${pkgbase}-${pkgver}/test/porousmediumflow/2p/cornerpoint/spatialparams.hh
  sed -i 's/^Version: '"${pkgver::3}"'-git/Version: '"${pkgver}"'/' ${pkgbase}-${pkgver}/dune.module
}

build() {
  cmake \
    -S ${pkgbase}-${pkgver} \
    -B build-cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DENABLE_HEADERCHECK=ON \
    -DDUNE_ENABLE_PYTHONBINDINGS=ON \
    -DCMAKE_DISABLE_FIND_PACKAGE_Vc=TRUE \
    -Wno-dev
  cmake --build build-cmake --target all
  cd build-cmake/python
  python setup.py build
}

package_dumux() {
  depends=("dune-grid>=${_dunever}" "dune-istl>=${_dunever}" "dune-localfunctions>=${_dunever}")
  DESTDIR="${pkgdir}" cmake --build build-cmake --target install
  install -Dm644 ${pkgbase}-${pkgver}/LICENSE.md "${pkgdir}/usr/share/licenses/${pkgbase}/LICENSE"
  find "${pkgdir}" -type d -empty -delete
}

package_python-dumux() {
  depends=("dumux>=${pkgver}" "python-dune-common>=${_dunever}")
  pkgdesc+=" (python bindings)"
  cd build-cmake/python
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
}
