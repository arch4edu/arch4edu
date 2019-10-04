# Maintainer: Baris Demirdelen <barisdemirdelen at gmail com>
# Previous maintainer: Andrew Anderson <aanderso@tcd.ie>
# Contributor: Jonathon Fernyhough <jonathon_at manjaro_dotorg>

pkgname=mkl-dnn
pkgver=1.1
pkgrel=1
pkgdesc="Intel® Math Kernel Library for Deep Neural Networks"
arch=(x86_64)
url=https://github.com/intel/mkl-dnn
license=('APACHE')
makedepends=('cmake>=2.8' 'doxygen>=1.8.5' 'graphviz')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intel/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('c5aac67e5ed4d95fe9943f835df49bbe6d608507780787c64aa620bdbd2171ba')

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
