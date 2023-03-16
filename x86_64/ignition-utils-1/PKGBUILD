# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Bernd Müller <github@muellerbernd.de>

pkgname=ignition-utils-1
pkgver=1.5.1
pkgrel=1
pkgdesc="Classes and functions for robot applications"
arch=('any')
url="https://gazebosim.org/libs/utils"
license=('Apache')
depends=('cmake' 'ignition-cmake-2')
provides=('ignition-utils=1')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/gazebosim/gz-utils/archive/ignition-utils1_${pkgver}.tar.gz")
sha256sums=('4bc6033c3616376b34298e02a3e2de77a5c479ab9f8aeaaddec924d56beb7df2')

_dir="gz-utils-ignition-utils1_${pkgver}"

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
