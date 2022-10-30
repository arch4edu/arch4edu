# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
pkgname=hipify-clang
pkgver=5.3.0
pkgrel=1
pkgdesc='Convert CUDA to Portable C++ Code'
arch=('x86_64')
url='https://docs.amd.com/bundle/HIP-Programming-Guide-v5.2/page/Transitioning_from_CUDA_to_HIP.html'
license=('MIT')
depends=('rocm-llvm' 'cuda')
makedepends=('cmake')
_git='https://github.com/ROCm-Developer-Tools/HIPIFY'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('7674900d2b9319d91fa8f469252c5acb5bedf339142417cdcb64f33ee8482e00')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake \
    -Wno-dev -B build \
    -S "$_dirname" \
    -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip/bin
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
