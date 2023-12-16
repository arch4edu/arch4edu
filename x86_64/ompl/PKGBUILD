# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Wil Thomason <wbthomason@cs.cornell.edu>
# Contributor: Sven Schneider <archlinux.sandmann@googlemail.com>

pkgname=ompl
pkgver=1.6.0
pkgrel=1
pkgdesc="The Open Motion Planning Library (OMPL) consists of many state-of-the-art sampling-based motion planning algorithms"
arch=('i686' 'x86_64')
url="http://ompl.kavrakilab.org/"
license=('BSD')
conflicts=('ompl-git')
replaces=('ompl-git')
depends=('boost-libs')
makedepends=('boost' 'cmake' 'ninja' 'pkgconf' 'eigen')
optdepends=('python: Python bindings'
            'py++: Python bindings'
            'ode: Plan using the Open Dynamics Engine'
            'pypy: Speed up generating Python bindings'
            'spot: Used for constructing finite automata from LTL formulae'
            'morse-simulator-git: MORSE simulation engine OMPL plugin'
            'triangle: Used to create triangular decompositions of polygonal 2D environments'
            'flann: Additional nearest-neighbor query backend'
            'python-numpy: Python bindings'
            'r: Running Planner Arena locally'
            'castxml: Python bindings'
            'pygccxml: Python bindings')
source=(https://github.com/ompl/ompl/archive/${pkgver}.tar.gz)
sha512sums=(d1024d7cc8e309a1df94a950be67eefae1e66abaccd6b6b8980939559aee3d73c05c838ab24c818b6b57ce6c4b3181fde7595d3d1dd36d6cd0c6d125338084ac)

build() {
  # NOTE: To get Python bindings, you currently need to install pyplusplus through pip3. The AUR
  # py++ package will *not* work. Hopefully that will get fixed soon...
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir -p build
  cd build

  # NOTE: -march=native causes test failures by slowing down PRM and PRMstar on AMD processors for
  # unknown reasons. Uncomment the following to remove it if you encounter this issue.
  # CXXFLAGS=$(echo $CXXFLAGS | sed 's/-march=native//g')
  cmake -G Ninja \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_INSTALL_LIBDIR=lib \
  -DCMAKE_EXE_LINKER_FLAGS="-llz4" \
  -DOMPL_REGISTRATION=Off ..
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
