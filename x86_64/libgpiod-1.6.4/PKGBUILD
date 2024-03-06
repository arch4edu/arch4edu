# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Greg Erwin <first name last name 256 at gmail dot com>

pkgname=libgpiod-1.6.4
pkgver=1.6.4
pkgrel=1
pkgdesc="C library and tools for interacting with the linux GPIO character device"
url="https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git"
arch=('x86_64')
license=('LGPL2.1')
depends=('python')
makedepends=('autoconf-archive' 'doxygen' 'help2man' 'python-setuptools')
conflicts=('libgpiod')
source=("$url/snapshot/libgpiod-$pkgver.tar.gz")
sha256sums=('829d4ac268df07853609d67cfc7f476e9aa736cb2a68a630be99e8fad197be0a')

build() {
  cd "libgpiod-$pkgver"
  ./autogen.sh \
    --prefix=/opt/libgpiod-1.6.4 \
    --enable-tools=yes \
    --enable-bindings-cxx \
    --enable-bindings-python
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package() {
  cd "libgpiod-$pkgver"
  make DESTDIR="$pkgdir" install
}
