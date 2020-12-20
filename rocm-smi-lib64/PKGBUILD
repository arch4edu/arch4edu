# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-smi-lib64
pkgver=4.0.0
pkgrel=1
pkgdesc="ROCm SMI LIB"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/rocm_smi_lib"
license=('custom:NCSAOSL')
depends=()
makedepends=('cmake')
options=(!staticlibs strip)
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz")
sha256sums=('93d19229b5a511021bf836ddc2a9922e744bf8ee52ee0e2829645064301320f4')

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
