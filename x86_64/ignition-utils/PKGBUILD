# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=ignition-utils
pkgver=2.0.0
pkgrel=2
pkgdesc="Classes and functions for robot applications"
arch=('any')
url="https://gazebosim.org/libs/utils"
license=('Apache')
depends=('cmake' 'ignition-cmake>=3')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/gazebosim/gz-utils/archive/gz-utils2_${pkgver}.tar.gz")
sha256sums=('af9e5b862e10aa0cedd97d9c5ca3eb9a443b7c9e560a083e8f0399e93e1cfafa')

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
