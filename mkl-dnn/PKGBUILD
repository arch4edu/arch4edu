# Maintainer: Baris Demirdelen <barisdemirdelen at gmail com>
# Previous maintainer: Andrew Anderson <aanderso@tcd.ie>
# Contributor: Jonathon Fernyhough <jonathon_at manjaro_dotorg>

pkgname=mkl-dnn
pkgver=0.17.1
pkgrel=1
_mklmlver=2019.0.1.20180928
pkgdesc="Intel® Math Kernel Library for Deep Neural Networks"
arch=(x86_64)
url=https://github.com/intel/mkl-dnn
license=('APACHE')
makedepends=('cmake>=2.8' 'doxygen>=1.8.5' 'graphviz')
optdepends=('intel-mkl: Intel MKL small library for Intel OpenMP linking'
            'intel-compiler-base: Intel OpenMP runtime linking')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intel/$pkgname/archive/v$pkgver.tar.gz"
        "https://github.com/intel/$pkgname/releases/download/v$pkgver/mklml_lnx_$_mklmlver.tgz")
sha256sums=('75777735458c9e03434d9b1b111b92bca4230427b8de890dd694039dc34480ed'
            'f00dc3b142a5be399bdeebd7e7ea369545a35d4fb84c86f98b6b048d72685295')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build external

  # "Take advantage of optimized matrix-matrix multiplication (GEMM) function
  #  from Intel MKL"
  ln -s "$srcdir"/mklml_lnx_$_mklmlver external/

  # Allow compilation to succeed despite warnings
  # sed -i '58s| -Werror||' cmake/platform.cmake
}

build() {
  cd "$srcdir/$pkgname-$pkgver/build"
  cmake -DCMAKE_INSTALL_PREFIX="$pkgdir"/usr ..
  make
  make doc
}

check() {
  cd "$srcdir/$pkgname-$pkgver/build"
  make test
}

package() {
  cd "$srcdir/$pkgname-$pkgver/build"
  make install
}
