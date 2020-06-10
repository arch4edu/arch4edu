# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=llvm-amdgpu
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=3.5.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('4878fa85473b24d88edcc89938441edc85d2e8a785e567b7bd7ce274ecc2fd9c')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    # building LLVM/Clang requires ~1.5G per unit
    THREADS=$(( ($(getconf _PHYS_PAGES) * $(getconf PAGESIZE)) / 1610612736 ))
    if [ "$THREADS" -lt 1 ]; then
        THREADS=1
    fi
    NPROC=$(nproc)
    if [ "$THREADS" -gt $(nproc) ]; then
        THREADS="$NPROC"
    fi

    cmake -DCMAKE_INSTALL_PREFIX='/opt/rocm/llvm' \
          -DLLVM_HOST_TRIPLE=$CHOST \
          -DLLVM_BUILD_UTILS=ON \
          -DLLVM_ENABLE_BINDINGS=OFF \
          -DLLVM_ENABLE_OCAMLDOC=OFF \
          -DLLVM_ENABLE_PROJECTS='llvm;clang;lld' \
          -DLLVM_TARGETS_TO_BUILD='AMDGPU;X86' \
          -DOCAMLFIND=NO \
          "$_dirname/llvm"
    MAKEFLAGS="$MAKEFLAGS -j$THREADS" make
}

check() {
    make check
}

package() {
    DESTDIR="$pkgdir" make install
}
