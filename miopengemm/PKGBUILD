# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=miopengemm
pkgver=3.7.0
pkgrel=1
pkgdesc="An OpenCL GEMM kernel generator"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpenGEMM"
license=('custom:NCSAOSL')
depends=('ocl-icd')
makedepends=('opencl-headers' 'cmake' 'ocl-icd' 'rocm-cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/archive/rocm-$pkgver.tar.gz")
sha256sums=('392b280ca564b120f6b24ec1fe8782cba08a8a5fb52938e8bc3dc887d3fd08fa')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/MIOpenGEMM-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
}
