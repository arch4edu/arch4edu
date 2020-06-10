# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Radeon Open Compute - compiler support'
pkgver=3.5.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=(z3 zlib)
makedepends=(cmake rocm-cmake rocm-device-libs llvm-amdgpu)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('25c963b46a82d76d55b2302e0e18aac8175362656a465549999ad13d07b689b9')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_PREFIX_PATH="/opt/rocm/llvm;/opt/rocm" \
        "$_dirname/lib/comgr"

  make
}

package() {
  DESTDIR="$pkgdir" make install
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
