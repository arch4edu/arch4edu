# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=ignition-utils
pkgver=2.2.0
pkgrel=1
pkgdesc="Classes and functions for robot applications"
arch=('any')
url="https://gazebosim.org/libs/utils"
license=('Apache')
depends=('cmake' 'ignition-cmake>=3')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/gazebosim/gz-utils/archive/gz-utils2_${pkgver}.tar.gz")
sha256sums=('15846369999e1269ab4dcb2f9fd2b4acdd162a69ae40a3f1cd3889437173d3aa')

_dir="gz-utils-gz-utils2_${pkgver}"

build() {
  cd "$srcdir/$_dir"

  mkdir -p build
  cd build

  cmake .. -DCMAKE_BUILD_TYPE="Release" \
           -DCMAKE_INSTALL_PREFIX="${pkgdir}/usr" \
           -DCMAKE_INSTALL_LIBDIR="lib" \
           -DBUILD_TESTING=OFF

  make
}

package() {
  cd "$srcdir/$_dir/build"
  make install
}
