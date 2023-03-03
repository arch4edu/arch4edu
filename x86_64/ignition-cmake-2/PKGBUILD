# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>

pkgname=ignition-cmake-2
pkgver=2.16.0
pkgrel=1
pkgdesc="A set of CMake modules that are used by the C++-based Gazebo projects."
arch=('any')
url="https://gazebosim.org/libs/cmake"
license=('Apache')
depends=('cmake' 'pkg-config' 'ruby-ronn' 'doxygen')
provides=('ignition-cmake=2')
source=("https://github.com/gazebosim/gz-cmake/archive/ignition-cmake2_${pkgver}.tar.gz")
sha256sums=('fcbe3de79b711fff8f8a94f24652e5d0e5d3cac8a79dd8f96e03c4b1886db3cc')

_dir="gz-cmake-ignition-cmake2_${pkgver}"

build() {
  cd "$srcdir/$_dir"

  mkdir -p build
  cd build

  cmake .. -Wno-dev \
           -DCMAKE_BUILD_TYPE="Release" \
           -DCMAKE_INSTALL_PREFIX="/usr" \
           -DCMAKE_INSTALL_LIBDIR="lib" \
           -DBUILD_TESTING=OFF

  make
}

package() {
  cd "$srcdir/$_dir/build"
  make DESTDIR="$pkgdir/" install
}
