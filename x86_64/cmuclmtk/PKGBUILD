# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

pkgname=cmuclmtk
pkgver=0.7
pkgrel=2
pkgdesc="Language model tools for CMU Sphinx"
arch=('x86_64')
url="https://cmusphinx.github.io/"
license=('BSD-3-Clause')
depends=('glibc')
source=(http://downloads.sourceforge.net/cmusphinx/$pkgname-$pkgver.tar.gz)
sha256sums=('d23e47f00224667c059d69ac942f15dc3d4c3dd40e827318a6213699b7fa2915')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  export CFLAGS="$CFLAGS -Wno-error=implicit-function-declaration -Wno-error=incompatible-pointer-types"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
  install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname/"
}
