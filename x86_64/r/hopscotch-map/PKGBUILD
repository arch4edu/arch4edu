# Maintainer: Adrien Wu <adrien.sf.wu@gmail.com>

pkgname=hopscotch-map
pkgver=2.4.0
pkgrel=1
pkgdesc="C++ implementation of a fast hash map and hash set using hopscotch hashing"
arch=(x86_64)
url="https://github.com/Tessil/hopscotch-map"
license=('MIT')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('c147d1f6af9559c0e91af3ecf62274404ce5fb35ce94d2234c080ccc7a5913de')

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
