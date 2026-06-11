# Maintainer: KNOSSOS team <knossosteam ät gmail.com>

_pkgname=quazip
pkgname=$_pkgname-qt5
pkgver=1.5
pkgrel=1
pkgdesc='C++ wrapper for the ZIP/UNZIP C package (qt5)'
url='https://stachenov.github.io/quazip/'
license=(LGPL-2.1-or-later)
arch=(x86_64)
depends=(bzip2 qt5-base zlib)
makedepends=(cmake ninja)
source=($_pkgname-$pkgver.tar.gz::https://github.com/stachenov/quazip/archive/v$pkgver.tar.gz)
sha256sums=('405b72b6e76c8987ff41a762523b8f64876ba406d8a831d268ee0b63f1369582')

build() {
  cmake -S $_pkgname-$pkgver -B build -G Ninja -DQUAZIP_QT_MAJOR_VERSION=5 -DQUAZIP_ENABLE_TESTS=TRUE -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

check() {
  ctest --test-dir build --output-on-failure
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
