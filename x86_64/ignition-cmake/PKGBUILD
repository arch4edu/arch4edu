# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>

pkgname=ignition-cmake
pkgver=3.0.1
pkgrel=1
pkgdesc="A set of CMake modules that are used by the C++-based Gazebo projects."
arch=('any')
url="https://gazebosim.org/libs/cmake"
license=('Apache')
depends=('cmake' 'pkg-config' 'ruby-ronn' 'doxygen')
source=("https://github.com/gazebosim/gz-cmake/archive/gz-cmake3_${pkgver}.tar.gz")
sha256sums=('d211e1a5384b33968a0b755dd6bded512f3e2957d2f04766ec17b0b5114201a0')

_dir="gz-cmake-gz-cmake3_${pkgver}"

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
