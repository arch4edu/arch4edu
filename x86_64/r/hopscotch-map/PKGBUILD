# Maintainer: Adrien Wu <adrien.sf.wu@gmail.com>

pkgname=hopscotch-map
pkgver=2.3.1
pkgrel=1
pkgdesc="C++ implementation of a fast hash map and hash set using hopscotch hashing"
arch=(x86_64)
url="https://github.com/Tessil/hopscotch-map"
license=('MIT')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('53dab49005cd5dc859f2546d0d3eef058ec7fb3b74fc3b19f4965a9a151e9b20')

build() {
  cd $pkgname-$pkgver
  cmake . \
      -Bbuild \
      -DCMAKE_INSTALL_PREFIX=/usr
  make -C build
}

package() {
  cd $pkgname-$pkgver
  DESTDIR="$pkgdir" make -C build install
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
