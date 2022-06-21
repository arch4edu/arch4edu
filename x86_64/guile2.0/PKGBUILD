# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>

pkgname=guile2.0
_pkgname=guile
pkgver=2.0.14
pkgrel=6
pkgdesc='Portable, embeddable Scheme implementation written in C'
url='https://www.gnu.org/software/guile/'
arch=(x86_64)
license=(GPL)
depends=(gmp libltdl ncurses texinfo libunistring gc libffi)
source=(https://ftp.gnu.org/pub/gnu/$_pkgname/$_pkgname-$pkgver.tar.gz{,.sig})
validpgpkeys=('3CE464558A84FDC69DB40CFB090B11993D9AEBB5' # Ludovic Courtès <ludo@gnu.org>
              'FF478FB264DE32EC296725A3DDC0F5358812F8F2') # Andy Wingo
md5sums=('333b6eec83e779935a45c818f712484e'
         'SKIP')

build() {
  cd $_pkgname-$pkgver
  ./configure --prefix=/usr \
    --disable-static  \
    --disable-error-on-warning \
    --program-suffix=2.0
  make
}

package() {
  make -C $_pkgname-$pkgver DESTDIR="$pkgdir" install
  rm "$pkgdir"/usr/lib/libguile-2.?.so.*-gdb.scm

  sed -i '1s/guile/guile2.0/' -i "$pkgdir/usr/bin/guile-config2.0"
  mv "$pkgdir"/usr/share/aclocal/guile.m4 "$pkgdir"/usr/share/aclocal/guile20.m4
  rm -rf "$pkgdir"/usr/share/info
}
