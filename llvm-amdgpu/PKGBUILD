# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=llvm-amdgpu
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=3.9.0
pkgrel=2
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('1ff14b56d10c2c44d36c3c412b190d3d8cd1bb12cfc7cd58af004c16fd9987d1')
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

package() {
    DESTDIR="$pkgdir" make install
}
