# Maintainer:  fedefranc <ffaur-at-duck-dot-com>
# Contributor: Stas Elensky <stas-at-flexsys-dot-com-dot-ua>
# Contributor: honzor 

pkgname=libmodbus
pkgver=3.1.11
pkgrel=2
pkgdesc="A Modbus library for Linux, Mac OS X, FreeBSD, QNX and Win32"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://libmodbus.org"
license=('LGPL-2.1-or-later')
depends=(glibc)
makedepends=(asciidoc xmlto)
options=(!libtool)
source=(https://github.com/stephane/libmodbus/releases/download/v$pkgver/libmodbus-$pkgver.tar.gz)
sha256sums=('15b4b2e0f68122c2da9b195de5c330489a9c97d40b4a95d2822378dc14d780e7')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:
