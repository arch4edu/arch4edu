# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocthrust
pkgver=3.5.0
pkgrel=2
pkgdesc='Port of the Thrust parallel algorithm library atop HIP/ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocthrust'
license=('Apache')
depends=('hip-rocclr' 'rocprim')
makedepends=('cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocThrust'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('0d1bac1129d17bb1259fd06f5c9cb4c1620d1790b5c295b866fb3442d18923cb')

build() {
  mkdir -p build
  cd build

  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF \
        "$srcdir/rocThrust-rocm-$pkgver"
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
}
