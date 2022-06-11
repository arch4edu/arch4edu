# $Id: PKGBUILD 204732 2014-01-26 09:43:39Z ronald $
# Maintainer: Tom Gundersen <teg@jklm.no>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>

pkgname=eigen2
pkgver=2.0.17
pkgrel=4
pkgdesc="A lightweight C++ template library for vector and matrix math, a.k.a. linear algebra"
arch=('any')
url='http://eigen.tuxfamily.org/index.php?title=Main_Page'
license=('GPL' 'LGPL3')
makedepends=('cmake' 'pkg-config')
source=("https://gitlab.com/libeigen/eigen/-/archive/${pkgver}/eigen-${pkgver}.tar.gz")
sha1sums=('fb18d990d142ee77cb3f2166219246f7e70103fc')

build() {
  cmake -S "$srcdir/${pkgname%2}-$pkgver" -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr
  make -C build
}

package() {
  make -C build DESTDIR="${pkgdir}" install
}
