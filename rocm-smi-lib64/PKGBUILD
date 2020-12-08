# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-smi-lib64
pkgver=3.10.0
pkgrel=1
pkgdesc="ROCm SMI LIB"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/rocm_smi_lib"
license=('custom:NCSAOSL')
depends=()
makedepends=('cmake')
options=(!staticlibs strip)
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz")
sha256sums=('8bb2142640d1c6bf141f19accf809e61377a6e0c0222e47ac4daa5da2c85ddac')

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
