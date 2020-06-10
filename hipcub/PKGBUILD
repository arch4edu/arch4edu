# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=hipcub
pkgver=3.5.0
pkgrel=2
pkgdesc='Header-only library on top of rocPRIM or CUB'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#hipcub'
license=('custom')
depends=('rocprim')
makedepends=('cmake' 'git' 'hip-rocclr')
_git='https://github.com/ROCmSoftwarePlatform/hipCUB'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('1eb2cb5f6e90ed1b7a9ac6dd86f09ec2ea27bceb5a92eeffa9c2123950c53b9d')

build() {
  mkdir -p build
  cd build

  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        "$srcdir/hipCUB-rocm-$pkgver"
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
  install -Dm644 "$srcdir/hipCUB-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
