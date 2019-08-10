# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=wiredtiger
# Upstream's versioning of wiredtiger is a mess.
# Current commit's README says 3.1.1, and is what's used here
# git describe --long shows: r3.7.3.r423.g4051e4941
# git describe --long --tags shows: mongodb.4.0.6.r23.g4051e4941
pkgver=3.1.1.20190808
_commit=48bf8dae7cd96286d176f14feebb7250dcfe1430
pkgrel=1
pkgdesc="High performance, scalable, production quality, NoSQL, Open Source extensible platform for data management"
arch=('x86_64')
url="http://source.wiredtiger.com/"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'gperftools')
makedepends=('aspell-en')
source=("$pkgname-$_commit.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$_commit.tar.gz")
sha512sums=('6bd1459b62b6856b7d09265d07694661dd826541223913f9491de8838a354b0dcde251d037d5387824f4fb9a57460fa9942a8376eec72bba0650abcca903ebb3')

prepare() {
  mv wiredtiger-{$_commit,$pkgver}
  sed -i 's/print\(.*\)$/print(\1)/' ${srcdir}/wiredtiger-${pkgver}/dist/wtperf_config.py
  sed -i 's/\\n/^^/g' ${srcdir}/wiredtiger-${pkgver}/src/docs/Doxyfile
}

build() {
  cd wiredtiger-$pkgver

  ./autogen.sh
  ./configure --prefix=/usr \
              --enable-leveldb \
              --enable-lz4 \
              --enable-tcmalloc \
              --enable-verbose \
              --with-builtins=snappy,zlib
  make
}

check() {
  cd wiredtiger-$pkgver
  make test
}

package() {
  cd wiredtiger-$pkgver
  make DESTDIR="$pkgdir" install
}
