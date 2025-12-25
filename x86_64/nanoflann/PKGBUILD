# Maintainer: David Wells <drwells.aur at fastmail dot com>

pkgname=nanoflann
pkgver=1.9.0
pkgrel=2
pkgdesc='a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees'
arch=('any')
url='https://github.com/jlblancoc/nanoflann'
license=('BSD')
depends=('eigen' 'python')
makedepends=('cmake' 'gtest')
source=("https://github.com/jlblancoc/nanoflann/archive/v${pkgver}.tar.gz"
        "test.patch")
sha256sums=('14dc863ec47d52ec3272b4fd409fd198a52e6cab58ece70b1da9c3dc2e478942'
            '1a669aaf17fbaad39252e3f17eb83523dc0e49ea141c7a3c6c011040865ffdb8')

prepare () {
    cd "$pkgname-$pkgver"
    patch -p1 -i "${srcdir}/test.patch"
}

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
