# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-device-libs
pkgver=3.8.0
pkgrel=1
pkgdesc='Radeon Open Compute - device libs'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
license=('custom:NCSAOSL')
makedepends=(cmake llvm-amdgpu)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('e82cc9a8eb7d92de02cabb856583e28f17a05c8cf9c97aec5275608ef1a38574')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    CC=/opt/rocm/llvm/bin/clang \
    cmake   -DCMAKE_INSTALL_PREFIX=/opt/rocm \
            -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm \
            "$_dirname"
    make
}

package() {
    DESTDIR="$pkgdir" make install
    install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
