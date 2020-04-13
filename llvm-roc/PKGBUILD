# Maintainer: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=llvm-roc
pkgdesc='Radeon Open Compute - LLVM toolchain (clang, lld)'
pkgver=3.3.0
pkgrel=2
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python)
source=("$url/archive/rocm-ocl-$pkgver.tar.gz")
sha256sums=('a2bef7042e8e2f2cd8548cb246b88322e1c77188839983dcac8312d56f544dc8')
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

    cmake -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX='/opt/rocm' \
          -DLLVM_HOST_TRIPLE=$CHOST \
          -DLLVM_BUILD_LLVM_DYLIB=ON \
          -DLLVM_BUILD_UTILS=OFF \
          -DLLVM_ENABLE_BINDINGS=OFF \
          -DLLVM_ENABLE_OCAMLDOC=OFF \
          -DLLVM_ENABLE_PROJECTS='clang;lld' \
          -DLLVM_LINK_LLVM_DYLIB=ON \
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
