# Maintainer: Christoph Bayer <chrbayer@criby.de>
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Fredy García <frealgagu at gmail dot com>

pkgname=wiredtiger
# Upstream's versioning of wiredtiger is a mess.
# Current commit's README says 3.1.1, and is what's used here
# git describe --long shows: r3.7.3.r423.g4051e4941
# git describe --long --tags shows: mongodb.4.0.6.r23.g4051e4941
pkgver=3.1.1.20190701
_commit=4a3194b043b8cffb5339c12e1554d0bd42ed1b1f
pkgrel=1
pkgdesc="High performance, scalable, production quality, NoSQL, Open Source extensible platform for data management"
arch=('x86_64')
url="http://source.wiredtiger.com/"
license=('GPL')
depends=('snappy' 'lz4' 'zlib' 'gperftools')
makedepends=('aspell-en')
source=("$pkgname-$_commit.tar.gz::https://github.com/wiredtiger/wiredtiger/archive/$_commit.tar.gz")
sha512sums=('09617821b1b5717eb6d5a17f2f714c42b9e8eaae77167d0b455d45caf269451da3ce6c787ec9d7329c4b0eceb4f1c4e7c592d5f53d28e0585efa5d576f3ac0af')

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
