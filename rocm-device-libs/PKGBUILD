# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-device-libs
pkgver=3.3.0
pkgrel=2
pkgdesc='Radeon Open Compute - device libs'
arch=('any')
url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
license=('custom:NCSAOSL')
makedepends=(cmake llvm-roc)
source=("$url/archive/rocm-ocl-$pkgver.tar.gz")
sha256sums=('706b08230790e08ca6a7a2fb7687d6131fd39a562148340e00fa37a6c06769c5')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm -DLLVM_DIR=/opt/rocm/lib/cmake/llvm "$_dirname"
    make
}

package() {
    DESTDIR="$pkgdir" make install
    install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
