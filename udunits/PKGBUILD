# Maintainer:  Martin C. Doege <mdoege at compuserve dot com>
# Contributor: TDY <tdy@archlinux.info>
# Contributor: Kaiting Chen <kaitocracy@gmail.com>
# Contributor: Anton Bazhenov <anton.bazhenov at gmail>

pkgname=udunits
pkgver=2.2.28
pkgrel=1
pkgdesc="A tool for calculations of physical quantities"
arch=('i686' 'x86_64')
url="http://www.unidata.ucar.edu/software/udunits/"
license=('MIT')
depends=('expat')
options=('!libtool')
install=udunits.install
source=(https://artifacts.unidata.ucar.edu/repository/downloads-udunits/$pkgname-$pkgver-Source.tar.gz)
sha256sums=('4cff332db4368c621998116603ad2d35cfd4a605e60a77e9a7270aed7d905711')

build() {
  cd "$srcdir/$pkgname-$pkgver-Source"
  ./configure --prefix=/usr --disable-static
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver-Source"
  make DESTDIR="$pkgdir" install
  ln -s libudunits2.so "$pkgdir/usr/lib/libudunits.so"
  ln -s libudunits2.so.0 "$pkgdir/usr/lib/libudunits.so.0"
  ln -s libudunits2.so.0.1.0 "$pkgdir/usr/lib/libudunits.so.0.1.0"
  install -Dm0644 COPYRIGHT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
