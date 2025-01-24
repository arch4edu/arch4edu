# Contributor: Graziano Giuliani <giuliani@lamma.rete.toscana.it>

pkgname=ncview
pkgver=2.1.11
pkgrel=1
pkgdesc="A visual browser for netCDF format files"
arch=(i686 x86_64)
url="https://cirrus.ucsd.edu/ncview/"
license=('GPL3')
depends=(netcdf udunits netpbm libxaw xorg-fonts-misc)
source=("https://cirrus.ucsd.edu/~pierce/ncview/${pkgname}-${pkgver}.tar.gz")
md5sums=('946e351ef6f50dab3d0a52092fe131d7')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  sed -i configure -e 's/libppm/libnetpbm/g'
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  CFLAGS="$CFLAGS -Wno-incompatible-pointer-types" CC="$(nc-config --cc)" CPPFLAGS="$CFLAGS" ./configure \
    --prefix=/usr \
    --with-ppm_incdir=/usr/include/netpbm \
    --with-ppm_libdir=/usr/lib
  make
}

package()
{
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install

  install -m755 -d "$pkgdir/usr/share/ncview"
  install -m644 *.ncmap "$pkgdir/usr/share/ncview"

  install -Dm644 Ncview-appdefaults "$pkgdir/usr/share/X11/app-defaults/Ncview"

  install -Dm644 data/ncview.1 "$pkgdir/usr/share/man/man1/ncview.1"
  gzip --best "$pkgdir/usr/share/man/man1/ncview.1"
}
