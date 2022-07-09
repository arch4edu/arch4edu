# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
pkgname=hipify-clang
pkgver=5.2.0
pkgrel=1
pkgdesc='Convert CUDA to Portable C++ Code '
arch=('x86_64')
url='https://docs.amd.com/bundle/HIP-Programming-Guide-v5.2/page/Transitioning_from_CUDA_to_HIP.html'
license=('MIT')
depends=('rocm-llvm' 'cuda')
makedepends=('cmake')
_git='https://github.com/ROCm-Developer-Tools/HIPIFY'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('dcd5f44daceb984bb654a209e78debf81e1cdeaf9202444a1e110b45ad6c3f4f')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -Wno-dev -B build \
        -S "$_dirname" \
        -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip/bin
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
