# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Radeon Open Compute - compiler support'
pkgver=3.9.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=(zlib llvm-amdgpu rocm-device-libs)
makedepends=(cmake rocm-cmake)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('6600e144d72dadb6d893a3388b42af103b9443755ce556f4e9e205ccd8ec0c83')
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
