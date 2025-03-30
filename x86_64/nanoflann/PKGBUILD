# Maintainer: David Wells <drwells.aur at fastmail dot com>

pkgname=nanoflann
pkgver=1.7.1
pkgrel=1
pkgdesc='a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees'
arch=('any')
url='https://github.com/jlblancoc/nanoflann'
license=('BSD')
depends=('eigen' 'python')
makedepends=('cmake' 'gtest')
source=("https://github.com/jlblancoc/nanoflann/archive/v${pkgver}.tar.gz")
sha256sums=('887e4e57e9c5fbf1c2937f9f5a9bc461c4786d54729b57a9c19547bdedb46986')

build() {
    rm -rf ${srcdir}/build
    mkdir ${srcdir}/build
    cd ${srcdir}/build

    cmake -DCMAKE_INSTALL_PREFIX="/usr/" ../$pkgname-$pkgver
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
