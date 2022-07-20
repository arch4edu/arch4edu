# Maintainer: Adrien Wu <adrien.sf.wu@gmail.com>

pkgname=hopscotch-map
pkgver=2.3.0
pkgrel=1
pkgdesc="C++ implementation of a fast hash map and hash set using hopscotch hashing"
arch=(x86_64)
url="https://github.com/Tessil/hopscotch-map"
license=('MIT')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('a59d65b552dc7682521989842418c92257147f5068152b5af50e917892ad9317')

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
