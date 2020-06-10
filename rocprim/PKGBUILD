# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocprim
pkgver=3.5.0
pkgrel=2
pkgdesc='Header-only library providing HIP parallel primitives'
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocPRIM"
license=('MIT')
depends=('hip-rocclr')
makedepends=('cmake' 'git')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('29302dbeb27ae88632aa1be43a721f03e7e597c329602f9ca9c9c530c1def40d')

build() {
  mkdir -p build
  cd build

  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF \
        -DBUILD_BENCHMARK=OFF \
        "$srcdir/rocPRIM-rocm-$pkgver"
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -Dm644 "$srcdir/rocPRIM-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
