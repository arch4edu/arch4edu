# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocr-debug-agent
pkgver=3.3.0
pkgrel=2
pkgdesc="ROCr Debug Agent Library"
arch=('x86_64')
url="https://github.com/ROCm-Developer-Tools/rocr_debug_agent"
license=('custom:NCSAOSL')
depends=("hsa-rocr" "hsakmt-roct" "rocm-clang-ocl")
makedepends=('cmake')
options=(!staticlibs strip)
source=("rocr_debug_agent-roc-$pkgver.tar.gz::https://github.com/ROCm-Developer-Tools/rocr_debug_agent/archive/roc-$pkgver.tar.gz")
sha256sums=('46a778fd7096d3affe65701f755b7ed7f9a2c611bad0b9a74302a56c66ee8ae2')

prepare() {
    sed -i 's/LC_BIN clang/LC_BIN clang-ocl/g' ${srcdir}/rocr_debug_agent-roc-$pkgver/src/CMakeLists.txt
    sed -i 's/opencl\/bin\/x86_64/bin/g' ${srcdir}/rocr_debug_agent-roc-$pkgver/src/CMakeLists.txt
}

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
