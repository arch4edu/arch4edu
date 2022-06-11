# Contributor: Graziano Giuliani <giuliani@lamma.rete.toscana.it>

pkgname=ncview
pkgver=2.1.8
pkgrel=1
pkgdesc="A visual browser for netCDF format files"
arch=(i686 x86_64)
url="http://meteora.ucsd.edu/~pierce/ncview_home_page.html"
license=('GPL3')
depends=(netcdf udunits netpbm libxaw)
source=("ftp://cirrus.ucsd.edu/pub/ncview/${pkgname}-${pkgver}.tar.gz")
md5sums=('510df57cd0b5fdae385d34c06b962b29')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  sed -i configure -e 's/libppm/libnetpbm/g'
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  CC="$(nc-config --cc)" CPPFLAGS="$CFLAGS" ./configure \
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
