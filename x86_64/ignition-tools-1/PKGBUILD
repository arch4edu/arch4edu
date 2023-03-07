# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>
# Contributor: marauder <abhinav.kssk@gmail.com>
pkgname=ignition-tools-1
pkgver=1.5.0
pkgrel=1
pkgdesc="Command line tools for the Gazebo libraries"
arch=('any')
url="https://gazebosim.org/libs/tools"
license=('Apache')
makedepends=('cmake' 'ignition-cmake' 'doxygen' 'pkg-config' 'ruby-ronn')
depends=('ruby')
provides=('ignition-tools=1')
source=("https://github.com/gazebosim/gz-tools/archive/ignition-tools_${pkgver}.tar.gz")
sha256sums=('cc99189063b6556e539836a438bdbb9da6eca1fe95a7058d46bfc17debc3d8f5')

_dir="gz-tools-ignition-tools_${pkgver}"

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
