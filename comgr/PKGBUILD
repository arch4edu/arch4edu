# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Radeon Open Compute - compiler support'
pkgver=3.8.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=(zlib llvm-amdgpu rocm-device-libs)
makedepends=(cmake rocm-cmake)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('62a35480dfabaa98883d91ed0f7c490daa9bbd424af37e07e5d85a6e8030b146')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_PREFIX_PATH="/opt/rocm/llvm;/opt/rocm" \
        "$_dirname/lib/comgr"

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
