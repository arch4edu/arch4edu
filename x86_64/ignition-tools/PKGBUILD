# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>
# Contributor: marauder <abhinav.kssk@gmail.com>
pkgname=ignition-tools
pkgver=2.0.0
pkgrel=2
pkgdesc="Command line tools for the Gazebo libraries"
arch=('any')
url="https://gazebosim.org/libs/tools"
license=('Apache')
makedepends=('cmake' 'ignition-cmake' 'doxygen' 'pkg-config' 'ruby-ronn')
depends=('ruby')
conflicts=('gazebo')
source=("https://github.com/gazebosim/gz-tools/archive/gz-tools2_${pkgver}.tar.gz")
sha256sums=('5e3788d5a1d5fa40724f1484cda716e0c050f01d2c516efa9f8a00877e74ef64')

_dir="gz-tools-gz-tools2_${pkgver}"

build() {
  cd "$srcdir/$_dir"

  mkdir -p build
  cd build

  cmake .. -DCMAKE_BUILD_TYPE="Release" \
           -DCMAKE_INSTALL_PREFIX="/usr" \
           -DCMAKE_INSTALL_LIBDIR="lib"

  make
}

package() {
  cd "$srcdir/$_dir/build"
  make DESTDIR="$pkgdir/" install
}
