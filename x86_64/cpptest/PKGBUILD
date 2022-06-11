# Maintainer: Steffen Weber <-boenki-gmx-de->
# Contributor: Juan Pablo Gonzalez Tognarelli <lord_jotape@yahoo.com.ar>

pkgname=cpptest
pkgver=2.0.0
pkgrel=1
pkgdesc="C++ Unit Testing Framework"
url="https://github.com/cpptest/cpptest"
license=('LGPL')
arch=('x86_64')
depends=('gcc-libs')
source=($pkgname-$pkgver.tar.gz::${url}/archive/${pkgver}.tar.gz)
md5sums=('3956c47d692f2dbdf22730a3f0c86310')

build() {
  cd "$pkgname-$pkgver"
  ./autogen.sh
  ./configure --prefix=/usr
  make
}

check() {
  cd "$pkgname-$pkgver"
  make check
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
