# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-smi-lib64
pkgver=3.8.0
pkgrel=1
pkgdesc="ROCm SMI LIB"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/rocm_smi_lib"
license=('custom:NCSAOSL')
depends=()
makedepends=('cmake')
options=(!staticlibs strip)
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz")
sha256sums=('86250c9ae9dfb18d4f7259a5f2f09b21574d4996fe5034a739ce63a27acd0082')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/rocm_smi_lib-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"
  make DESTDIR="$pkgdir" install
}
