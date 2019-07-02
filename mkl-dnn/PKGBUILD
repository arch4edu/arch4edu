# Maintainer: Baris Demirdelen <barisdemirdelen at gmail com>
# Previous maintainer: Andrew Anderson <aanderso@tcd.ie>
# Contributor: Jonathon Fernyhough <jonathon_at manjaro_dotorg>

pkgname=mkl-dnn
pkgver=0.20
pkgrel=1
_mklmlver=2019.0.5.20190502
pkgdesc="Intel® Math Kernel Library for Deep Neural Networks"
arch=(x86_64)
url=https://github.com/intel/mkl-dnn
license=('APACHE')
makedepends=('cmake>=2.8' 'doxygen>=1.8.5' 'graphviz' 'patchelf')
optdepends=('intel-mkl: Intel MKL small library for Intel OpenMP linking'
            'intel-compiler-base: Intel OpenMP runtime linking')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intel/$pkgname/archive/v$pkgver.tar.gz"
        "https://github.com/intel/$pkgname/releases/download/v$pkgver/mklml_lnx_$_mklmlver.tgz")
sha256sums=('52e111fefbf5a38e36f7bae7646860f7cbc985eba0725768f3fee8cdb31a9977'
            'a936d6b277a33d2a027a024ea8e65df62bd2e162c7ca52c48486ed9d5dc27160')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build external

  # "Take advantage of optimized matrix-matrix multiplication (GEMM) function
  #  from Intel MKL"

  ln -sf "$srcdir"/mklml_lnx_$_mklmlver external/

  # Allow compilation to succeed despite warnings
  # sed -i '66s|-Werror||' cmake/platform.cmake
}

build() {
  cd "$srcdir/$pkgname-$pkgver/build"
  cmake -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" -DCMAKE_INSTALL_LIBDIR="lib" -DCMAKE_INSTALL_RPATH="/usr/lib/mklml" -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE ..
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
  mkdir -p $pkgdir/usr/lib/mklml
  
  # Move libiomp5 so that it doesnt conflict with openmp package
  mv "$pkgdir/usr/lib/libiomp5.so" "$pkgdir/usr/lib/mklml"  
  patchelf --set-rpath /usr/lib/mklml "$pkgdir/usr/lib/libmklml_intel.so"
}
