# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-debug-agent
pkgver=3.5.0
pkgrel=1
pkgdesc="ROCr Debug Agent Library"
arch=('x86_64')
url="https://github.com/ROCm-Developer-Tools/rocr_debug_agent"
license=('custom:NCSAOSL')
depends=("hsa-rocr" "hsakmt-roct" "rocm-clang-ocl")
makedepends=('cmake')
options=(!staticlibs strip)
source=("$pkgname-$pkgver.tar.gz::https://github.com/ROCm-Developer-Tools/rocr_debug_agent/archive/roc-$pkgver.tar.gz")
sha256sums=('203ccb18d2ac508aae40bf364923f67375a08798b20057e574a0c5be8039f133')

prepare() {
    sed -i 's/LC_BIN clang/LC_BIN clang-ocl/g' ${srcdir}/rocr_debug_agent-roc-$pkgver/src/CMakeLists.txt
    sed -i 's/opencl\/bin\/x86_64/bin/g' ${srcdir}/rocr_debug_agent-roc-$pkgver/src/CMakeLists.txt
}

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocr_debug_agent \
        "$srcdir/rocr_debug_agent-roc-$pkgver/src"
  make
}

package() {
  cd "$srcdir/build"
  make DESTDIR="$pkgdir" install
}
