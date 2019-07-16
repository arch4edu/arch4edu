# Maintainer: Baris Demirdelen <barisdemirdelen at gmail com>
# Previous maintainer: Andrew Anderson <aanderso@tcd.ie>
# Contributor: Jonathon Fernyhough <jonathon_at manjaro_dotorg>

pkgname=mkl-dnn
pkgver=1.0
pkgrel=1
pkgdesc="Intel® Math Kernel Library for Deep Neural Networks"
arch=(x86_64)
url=https://github.com/intel/mkl-dnn
license=('APACHE')
makedepends=('cmake>=2.8' 'doxygen>=1.8.5' 'graphviz')
optdepends=()
source=("$pkgname-$pkgver.tar.gz::https://github.com/intel/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('27fd9da9720c452852f1226581e7914efcf74e1ff898468fdcbe1813528831ba')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build 

  # Allow compilation to succeed despite warnings
  # sed -i '66s|-Werror||' cmake/platform.cmake
}

build() {
  cd "$srcdir/$pkgname-$pkgver/build"
  cmake -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" -DCMAKE_INSTALL_LIBDIR="lib" ..
  make
  make doc
}

check() {
  cd "$srcdir/$pkgname-$pkgver/build"
  ctest
}

package() {
  cd "$srcdir/$pkgname-$pkgver/build"
  make install
}
