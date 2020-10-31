# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=miopengemm
pkgver=3.9.0
pkgrel=1
pkgdesc="An OpenCL GEMM kernel generator"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpenGEMM"
license=('custom:NCSAOSL')
depends=('ocl-icd')
makedepends=('opencl-headers' 'cmake' 'ocl-icd' 'rocm-cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/archive/rocm-$pkgver.tar.gz")
sha256sums=('8e1273c35d50e9fd92e303d9bcbdd42ddbfda20844b3248428e16b54928f6dc2')

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
