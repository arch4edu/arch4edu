# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocr-debug-agent
pkgver=3.1.0
pkgrel=1
pkgdesc="ROCr Debug Agent Library"
arch=('x86_64')
url="https://github.com/ROCm-Developer-Tools/rocr_debug_agent"
license=('custom:NCSAOSL')
depends=("rocr-runtime>=$pkgver" "roct-thunk-interface>=$pkgver")
makedepends=('cmake')
options=(!staticlibs strip)
source=("rocr_debug_agent-roc-$pkgver.tar.gz::https://github.com/ROCm-Developer-Tools/rocr_debug_agent/archive/roc-$pkgver.tar.gz")
sha256sums=('3ee1e947bee5d89c4f0bb6136be9306bcee0088c0b9534bd5065cad31fecac27')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocr_debug_agent \
        "$srcdir/rocr_debug_agent-roc-$pkgver/src"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
}
