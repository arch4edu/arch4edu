# Maintainer: Baris Demirdelen <barisdemirdelen at gmail com>
# Previous maintainer: Andrew Anderson <aanderso@tcd.ie>
# Contributor: Jonathon Fernyhough <jonathon_at manjaro_dotorg>

pkgname=mkl-dnn
pkgver=0.18
pkgrel=1
_mklmlver=2019.0.3.20190220
pkgdesc="Intel® Math Kernel Library for Deep Neural Networks"
arch=(x86_64)
url=https://github.com/intel/mkl-dnn
license=('APACHE')
makedepends=('cmake>=2.8' 'doxygen>=1.8.5' 'graphviz')
optdepends=('intel-mkl: Intel MKL small library for Intel OpenMP linking'
            'intel-compiler-base: Intel OpenMP runtime linking')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intel/$pkgname/archive/v$pkgver.tar.gz"
        "https://github.com/intel/$pkgname/releases/download/v$pkgver/mklml_lnx_$_mklmlver.tgz")
sha256sums=('38a1c02104ee9f630c1ad68164119cd58ad0aaf59e04ccbe7bd5781add7bfbea'
            'f4129843d5c2996419f96f10928edd02b2150998861a088dc7cfa1b6a058102a')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p build external

  # "Take advantage of optimized matrix-matrix multiplication (GEMM) function
  #  from Intel MKL"

  ln -sf "$srcdir"/mklml_lnx_$_mklmlver external/

  # Allow compilation to succeed despite warnings
  # sed -i '58s| -Werror||' cmake/platform.cmake
}

build() {
  cd "$srcdir/$pkgname-$pkgver/build"
  cmake -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" ..
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
  mv "$pkgdir/usr/lib64" "$pkgdir/usr/lib" 
}
