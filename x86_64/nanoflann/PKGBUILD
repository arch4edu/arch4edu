# Maintainer: David Wells <drwells.aur at fastmail dot com>

pkgname=nanoflann
pkgver=1.12.1
pkgrel=2
pkgdesc='a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees'
arch=('any')
url='https://github.com/jlblancoc/nanoflann'
license=('BSD')
depends=('eigen' 'python')
makedepends=('cmake' 'gtest')
source=("https://github.com/jlblancoc/nanoflann/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('f4884bc47cdf175700ba1437293d4fadff1b8db5d968550899c63f7144f9034b')

build() {
    rm -rf ${srcdir}/build
    mkdir ${srcdir}/build
    cd ${srcdir}/build

    cmake -DNANOFLANN_USE_SYSTEM_GTEST=ON -DCMAKE_INSTALL_PREFIX="/usr/" ../$pkgname-$pkgver
    make ${MAKEFLAGS}
}

check() {
    cd $srcdir/build
    make test
}

package() {
  cd $srcdir/build
  make DESTDIR="$pkgdir" install

  install -Dm644 $srcdir/$pkgname-$pkgver/COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}

# vim:set ts=2 sw=2 et:
