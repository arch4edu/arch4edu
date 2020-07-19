# Maintainer: Peter Mattern <pmattern at arcor dot de>
# Contributor: Xiao-Long Chen <chenxiaolong at cxl.epac.to>

pkgname=charls
pkgver=2.1.0
pkgrel=1
pkgdesc='A C++ JPEG-LS library implementation'
arch=('i686' 'x86_64')
url='https://github.com/team-charls/charls'
license=('BSD')
makedepends=('cmake' 'dos2unix')
source=("$pkgname-$pkgver.tar.gz::https://github.com/team-charls/$pkgname/archive/$pkgver.tar.gz")
sha256sums=('0d6af23928ba4f1205b1b74754111e5f5f6b47d192199ffa7a70d14b824ad97d')

prepare() {
  # remove CRLF sequence
  for i in $(find $pkgname-$pkgver -type f -exec file {} \; | grep CRLF | sed 's/:.*$//')
  do
    dos2unix $i
  done
}

build() {
  mkdir -p build
  cd build
  cmake $srcdir/$pkgname-$pkgver -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
  install -D -m644 $srcdir/$pkgname-$pkgver/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
