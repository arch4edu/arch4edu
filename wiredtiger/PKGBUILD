# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Christoph Bayer <chrbayer@criby.de>
# Contributor: James P. Harvey <jamespharvey20 at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=wiredtiger
pkgver=10.0.0
pkgrel=1
pkgdesc="High performance NoSQL platform"
arch=('x86_64')
url="https://source.wiredtiger.com"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'zstd' 'gperftools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$pkgver.tar.gz")
sha512sums=('6e2d0fa1e20467ce6d39d4ac097b0bad9954e10f6ff72dc35b02871f9ce5492a889899560065dfdf8d60f966f1d3cf0b3b8490ab017a4199bdcab9d190e77bb0')
b2sums=('2b9b85bd7711c114a9b6e3c8cd0db3ce8ba6d08efd3b7b8e39ceff8cd251147c9d9a13942353ec885b7542f732d25946befd814fc046225bfde6ae6d31097c10')

build() {
  cd "$pkgname-$pkgver"
  ./autogen.sh
  ./configure \
    --prefix=/usr \
    --enable-tcmalloc \
    --with-builtins=snappy,lz4,zlib,zstd

}

package() {
	cd "$pkgname-$pkgver"

  # NOTE there is no `make` in build() because it compiles & runs broken tests
  make DESTDIR="$pkgdir" install
}
