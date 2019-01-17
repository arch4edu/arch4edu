# Maintainer: Baris Demirdelen <barisdemirdelen at gmail com>
# Previous maintainer: Andrew Anderson <aanderso@tcd.ie>
# Contributor: Jonathon Fernyhough <jonathon_at manjaro_dotorg>

pkgname=mkl-dnn
pkgver=0.17.2
pkgrel=1
_mklmlver=2019.0.1.20181227
pkgdesc="Intel® Math Kernel Library for Deep Neural Networks"
arch=(x86_64)
url=https://github.com/intel/mkl-dnn
license=('APACHE')
makedepends=('cmake>=2.8' 'doxygen>=1.8.5' 'graphviz')
optdepends=('intel-mkl: Intel MKL small library for Intel OpenMP linking'
            'intel-compiler-base: Intel OpenMP runtime linking')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intel/$pkgname/archive/v$pkgver.tar.gz"
        "https://github.com/intel/$pkgname/releases/download/v$pkgver/mklml_lnx_$_mklmlver.tgz")
sha256sums=('56c3e22d4fad816059cc58fd8e78ab3bacbec76a6bbded7eaead66220d8e5134'
            '0a8b39dd63494b1c5f55ef0eb7cd9a4f8cc3bcba09177b20a078c2b47e00f677')

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
