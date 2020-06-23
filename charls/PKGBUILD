# Maintainer: Peter Mattern <pmattern at arcor dot de>
# Contributor: Xiao-Long Chen <chenxiaolong at cxl.epac.to>

pkgname=charls
pkgver=2.0.0
pkgrel=1
pkgdesc='A C++ JPEG-LS library implementation'
arch=('i686' 'x86_64')
url='https://github.com/team-charls/charls'
license=('BSD')
makedepends=('cmake' 'dos2unix')
source=("$pkgname-$pkgver.tar.gz::https://github.com/team-charls/$pkgname/archive/$pkgver.tar.gz")
sha256sums=("528c6a3cc168a44e73f2890d8f4a35104a54d752eba3d6a643f050b72dd67cfa")

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
  install -D -m644 $srcdir/$pkgname-$pkgver/License.txt $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
