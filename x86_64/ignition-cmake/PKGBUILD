# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Tim Rakowski <tim.rakowski@gmail.com>

pkgname=ignition-cmake
pkgver=2.14.0
pkgrel=1
pkgdesc="Provides modules that are used to find dependencies of ignition projects and generate cmake targets for consumers of ignition projects to link against."
arch=('any')
url="https://gazebosim.org/libs/cmake"
license=('Apache')
depends=('cmake' 'pkg-config' 'ruby-ronn' 'doxygen')
optdepends=()
conflicts=()
source=("https://github.com/gazebosim/gz-cmake/archive/${pkgname}2_${pkgver}.tar.gz")
sha256sums=('c4ffbc3252703df8e4f95b5f9aae05f776e558b3a3503b517ce99ff18ff1059c')

_dir="gz-cmake-${pkgname}2_${pkgver}"

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
