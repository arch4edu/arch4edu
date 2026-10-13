# Maintainer: David Wells <drwells.aur at fastmail dot com>

pkgname=nanoflann
pkgver=2.0.1
pkgrel=1
pkgdesc='a C++ header-only library for Nearest Neighbor (NN) search wih KD-trees'
arch=('any')
url='https://github.com/jlblancoc/nanoflann'
license=('BSD')
depends=('eigen' 'python')
makedepends=('cmake' 'gtest')
source=("https://github.com/jlblancoc/nanoflann/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('bb3991ad924248d3f20953a951c34878196c11ca112d800acc341c3808443896')


prepare () {
    sed -i '/EIGEN3_INCLUDE_DIR/d' ${srcdir}/${pkgname}-${pkgver}/tests/CMakeLists.txt
    sed -i 's/Threads::Threads/Threads::Threads Eigen3::Eigen/' ${srcdir}/${pkgname}-${pkgver}/tests/CMakeLists.txt
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
