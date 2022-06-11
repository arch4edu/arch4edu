# Maintainer: Heavysink <winstonwu91 at gmail>
pkgname=libcsa-git
pkgver=20191025.917fa3c
pkgrel=1
pkgdesc="Bivariate Cubic Spline approximation library + standalone utility"
arch=(i686 x86_64)
url="https://github.com/sakov/csa-c"
license=('GPL3')
depends=('glibc')
makedepends=('git')
source=($pkgname::"git+https://github.com/sakov/csa-c.git")
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$pkgname/"
    (git log -1 --format='%cd.%h' --date=short | tr -d -)
}

build() {
  cd "$srcdir/$pkgname/csa"
  export CFLAGS+=" -fPIC"
  ./configure \
    --prefix=$pkgdir/usr
  make
}

package()
{
  cd "$srcdir/$pkgname/csa"
  make install
}
