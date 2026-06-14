# Maintainer: Greg Land <landjgregory at gmail dot com>
# Contributor: Tarn Burton <twburton at gmail dot com>
pkgname=xeus
pkgver=5.2.3
pkgrel=1
pkgdesc="C++ implementation of the Jupyter kernel protocol"
arch=("x86_64")
url="https://github.com/QuantStack/xeus"
license=('BSD')
depends=('openssl' 'crypto++' 'nlohmann-json' 'xtl' 'zeromq')
makedepends=('cmake' 'zeromq' 'cppzmq')
source=("$pkgname-$pkgver.tar.gz::https://github.com/QuantStack/xeus/archive/$pkgver.tar.gz")
sha256sums=('37dfe990319901b3ad7f6ee7f5789bfc324e2d440ae821c1ea72a0b716de2103')
options=(staticlibs)

build() {
  cd "$pkgname-$pkgver"
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..
  make
}

package() {
  cd "$pkgname-$pkgver/build"
  make DESTDIR="${pkgdir}" install
}
