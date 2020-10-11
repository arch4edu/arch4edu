# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=llvm-amdgpu
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=3.8.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('93a28464a4d0c1c9f4ba55e473e5d1cde4c5c0e6d087ec8a0a3aef1f5f5208e8')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake -Wno-dev -S "$_dirname/llvm" \
          -DCMAKE_INSTALL_PREFIX='/opt/rocm/llvm' \
          -DCMAKE_BUILD_TYPE=Release \
          -DLLVM_HOST_TRIPLE=$CHOST \
          -DLLVM_BUILD_UTILS=ON \
          -DLLVM_ENABLE_BINDINGS=OFF \
          -DLLVM_ENABLE_OCAMLDOC=OFF \
          -DLLVM_ENABLE_PROJECTS='llvm;clang;compiler-rt;lld' \
          -DLLVM_TARGETS_TO_BUILD='AMDGPU;X86' \
          -DOCAMLFIND=NO
    make
}

check() {
    make check
}

package() {
    DESTDIR="$pkgdir" make install
}
