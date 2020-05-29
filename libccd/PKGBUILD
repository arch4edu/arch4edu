# Previous Maintainer: Benjamin Chretien <chretien at lirmm dot fr>
# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=libccd
pkgver=2.1
pkgrel=1
pkgdesc="Library for collision detection between two convex shapes."
arch=('i686' 'x86_64')
url='https://github.com/danfis/libccd'
license=('BSD')
depends=()
makedepends=('cmake')
source=(https://github.com/danfis/libccd/archive/v${pkgver}.tar.gz)
sha256sums=('542b6c47f522d581fbf39e51df32c7d1256ac0c626e7c2b41f1040d4b9d50d1e')
provides=('libccd')
conflicts=('libccd-git')

_dir=libccd-${pkgver}

build() {
  rm -rf ${srcdir}/build && mkdir -p ${srcdir}/build
  cd ${srcdir}/build

  cmake ${srcdir}/${_dir} \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release

  make
}

package() {
  cd "${srcdir}/build"

  make DESTDIR="${pkgdir}/" install
}
