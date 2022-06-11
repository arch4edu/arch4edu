# Maintainer:  Martin C. Doege <mdoege at compuserve dot com>
# Contributor: TDY <tdy@archlinux.info>
# Contributor: Kaiting Chen <kaitocracy@gmail.com>
# Contributor: Anton Bazhenov <anton.bazhenov at gmail>

pkgname=udunits
pkgver=2.2.28
pkgrel=3
pkgdesc="A tool for calculations of physical quantities"
arch=('i686' 'x86_64')
url="http://www.unidata.ucar.edu/software/udunits/"
license=('MIT')
depends=('expat')
options=('!libtool')
install=udunits.install
source=(https://artifacts.unidata.ucar.edu/repository/downloads-udunits/$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('590baec83161a3fd62c00efa66f6113cec8a7c461e3f61a5182167e0cc5d579e')

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
