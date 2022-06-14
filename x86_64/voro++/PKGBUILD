# Maintainer: xpt <user.xpt@gmail.com>
pkgname=voro++
pkgver=0.4.6
pkgrel=2
pkgdesc="A free software library for the computation of three dimensional Voronoi cells."
arch=('i686' 'x86_64')
url="http://math.lbl.gov/voro++/"
license=('BSD')
depends=('perl' 'gcc-libs')
options=(staticlibs)
source=(https://download.lammps.org/thirdparty/${pkgname}-$pkgver.tar.gz)
md5sums=('2338b824c3b7b25590e18e8df5d68af9')
 
build() {
  cd "$srcdir/$pkgname-$pkgver"
  sed -i 's/(PREFIX)\/man/(PREFIX)\/share\/man/g' Makefile
  sed -i 's/-Wall/-Wall -fPIC/g' config.mk
  make all
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make PREFIX=$pkgdir/usr install
  install -d $pkgdir/usr/share/licenses/$pkgname $pkgdir/usr/share/$pkgname/{examples,scripts} $pkgdir/usr/share/doc/$pkgname/{,html}
  install -m644 $srcdir/$pkgname-$pkgver/LICENSE $pkgdir/usr/share/licenses/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/NEWS $pkgdir/usr/share/doc/$pkgname
  install -m644 $srcdir/$pkgname-$pkgver/scripts/* $pkgdir/usr/share/$pkgname/scripts
  install -m644 $srcdir/$pkgname-$pkgver/html/* $pkgdir/usr/share/doc/$pkgname/html
  cp -r $srcdir/$pkgname-$pkgver/examples/* $pkgdir/usr/share/$pkgname/examples
  chmod -R 755 $pkgdir/usr/share/$pkgname/examples
} 
