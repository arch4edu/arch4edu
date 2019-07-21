# Maintainer:  Martin C. Doege <mdoege at compuserve dot com>
# Contributor: TDY <tdy@archlinux.info>
# Contributor: Kaiting Chen <kaitocracy@gmail.com>
# Contributor: Anton Bazhenov <anton.bazhenov at gmail>

pkgname=udunits
pkgver=2.2.26
pkgrel=1
pkgdesc="A tool for calculations of physical quantities"
arch=('i686' 'x86_64')
url="http://www.unidata.ucar.edu/software/udunits/"
license=('MIT')
depends=('expat')
options=('!libtool')
install=udunits.install
source=(ftp://ftp.unidata.ucar.edu/pub/$pkgname/$pkgname-$pkgver.tar.gz)
sha256sums=('368f4869c9c7d50d2920fa8c58654124e9ed0d8d2a8c714a9d7fdadc08c7356d')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr --disable-static
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  ln -s libudunits2.so "$pkgdir/usr/lib/libudunits.so"
  ln -s libudunits2.so.0 "$pkgdir/usr/lib/libudunits.so.0"
  ln -s libudunits2.so.0.1.0 "$pkgdir/usr/lib/libudunits.so.0.1.0"
  install -Dm0644 COPYRIGHT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
