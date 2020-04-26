# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Radeon Open Compute - compiler support'
pkgver=3.3.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=(llvm-amdgpu)
makedepends=(cmake rocm-cmake rocm-device-libs)
source=("$url/archive/rocm-$pkgver.tar.gz"
        "comgr-find-lld-includes.patch")
sha256sums=('01e2524e0f28ecd6f46c9720f279207de935d826b0172158792aa3ec86af9ca7'
            '4571b16961f15249e8cc8b9a9ae7f0863600345aa5e95959192149eacdb01d2e')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
  patch -uN ${srcdir}/${_dirname}/lib/comgr/CMakeLists.txt comgr-find-lld-includes.patch
}

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
