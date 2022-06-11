# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
pkgdesc="Flexible Collision Library."
url='https://github.com/flexible-collision-library/fcl'
pkgname=fcl
pkgver=0.7.0
arch=('i686' 'x86_64')
pkgrel=1
license=('BSD')
makedepends=('cmake' 'octomap')
depends=('libccd' 'eigen')
optdepends=('octomap: collision detection with octrees'
            'tinyxml: support for global penetration depth test'
            'flann: support for fast approximate nearest neighbor searches')
_dir=fcl-${pkgver}
source=(https://github.com/flexible-collision-library/fcl/archive/${pkgver}.tar.gz)
sha256sums=('90409e940b24045987506a6b239424a4222e2daf648c86dd146cbcb692ebdcbc')

build() {
  mkdir -p ${srcdir}/build
  cd ${srcdir}/build

  cmake ${srcdir}/${_dir} \
    -DCMAKE_INSTALL_PREFIX="/usr" \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_BUILD_TYPE="Release"

  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}
