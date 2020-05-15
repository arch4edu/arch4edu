# Maintainer: Heavysink <winstonwu91 at gmail>
pkgname=libnn-git
pkgver=20191024.ea3e390
pkgrel=1
pkgdesc="a C code for Natural Neighbours interpolation of 2D scattered data"
arch=(i686 x86_64)
url="https://github.com/sakov/nn-c"
license=('GPL3')
depends=('glibc')
makedepends=('git')
source=($pkgname::"git://github.com/sakov/nn-c.git")
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$pkgname/"
    (git log -1 --format='%cd.%h' --date=short | tr -d -)
}

build() {
  cd "$srcdir/$pkgname/nn"
  export CFLAGS+=" -fPIC"
  ./configure \
    --prefix=$pkgdir/usr
  make
}

package()
{
  cd "$srcdir/$pkgname/nn"
  make install
}
