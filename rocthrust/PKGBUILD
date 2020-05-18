# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocthrust
pkgver=3.3.0
pkgrel=4
pkgdesc='Port of the Thrust parallel algorithm library atop HIP/ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocthrust'
license=('Apache')
depends=('hip-hcc' 'rocprim')
makedepends=('cmake' 'git' 'hcc')
_git='https://github.com/ROCmSoftwarePlatform/rocThrust'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('5782c9b96233b2050168381b3c2259baeb410b859f68c25b2d14110fb1bb726f')

build() {
  mkdir -p build
  cd build

  CXX=/opt/rocm/hcc/bin/hcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocthrust \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF \
        "$srcdir/rocThrust-rocm-$pkgver"
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/opt/rocm/include"
  ln -s /opt/rocm/rocthrust/include/thrust "$pkgdir/opt/rocm/include"
}
