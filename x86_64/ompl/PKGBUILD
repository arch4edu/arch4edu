# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Wil Thomason <wbthomason@cs.cornell.edu>
# Contributor: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=ompl
pkgver=2.0.0
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
sha512sums=(8da42719399b2512395463c7c3336147b9b215fa069aeb9ea38ede1a7f52f0a7d3ed1701a8c7d3db08b6b86f18c2d644f7896eecdd746ba5fc95b0e08c9d7441)

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
