# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Wil Thomason <wbthomason@cs.cornell.edu>
# Contributor: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=ompl
pkgver=2.0.2
pkgrel=1
pkgdesc="The Open Motion Planning Library (OMPL) consists of many state-of-the-art sampling-based motion planning algorithms"
arch=('i686' 'x86_64')
url="http://ompl.kavrakilab.org/"
license=('BSD')
conflicts=('ompl-git')
replaces=('ompl-git')
depends=('boost-libs' 'eigen')
makedepends=('boost' 'cmake' 'ninja' 'pkgconf' 'eigen')
optdepends=('ode: Plan using the Open Dynamics Engine'
            'spot: Used for constructing finite automata from LTL formulae'
            'morse-simulator-git: MORSE simulation engine OMPL plugin'
            'triangle: Used to create triangular decompositions of polygonal 2D environments'
            'flann: Additional nearest-neighbor query backend'
            'r: Running Planner Arena locally')
source=(https://github.com/ompl/ompl/archive/${pkgver}.tar.gz)
sha512sums=('21e6e1bbc679f548aa11fa27fd9e4683ed6227849da8dcc7cae8dc912e807374f0e990d3435bcbb8c4c212196f6aecbf400b4546ad2b190cac461cd3b44bee8c')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir -p build
  cd build

  # NOTE: -march=native causes test failures by slowing down PRM and PRMstar on AMD processors for
  # unknown reasons. Uncomment the following to remove it if you encounter this issue.
  # CXXFLAGS=$(echo $CXXFLAGS | sed 's/-march=native//g')
  # NOTE: VAMP and Python bindings require git submodules that are not present in the release
  # tarball, so they must be disabled here.
  cmake -G Ninja \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_INSTALL_LIBDIR=lib \
  -DCMAKE_EXE_LINKER_FLAGS="-llz4" \
  -DOMPL_REGISTRATION=Off \
  -DOMPL_BUILD_VAMP=OFF \
  -DOMPL_BUILD_PYTHON_BINDINGS=OFF ..
  cmake --build .
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  ctest
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cd build
  DESTDIR=${pkgdir} ninja install
}
