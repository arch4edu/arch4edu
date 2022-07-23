# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=rocm-llvm-mlir
pkgdesc="Radeon Open Compute - LLVM Multi-Level IR Compiler Framework"
pkgver=5.3.0
pkgrel=1
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/llvm-project-mlir"
license=('custom:Apache 2.0 with LLVM Exception')
depends=("hip")
makedepends=("cmake" "sqlite" "python")
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/rocm-$pkgver.tar.gz"
        "llvm-project-mlir-fix-rpath-flags.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/llvm-project-mlir/pull/688.patch")
sha256sums=('ee5093aad5459773c350205ef937a186a20994b42798106f8126b9914ad099a5'
            '7085543c8726b3b14cae675ecccef54847a2525af3a13d34d6e1d52d2a17907a')
options=(!lto)
_dirname="$(basename $url)-$(basename ${source[0]} .tar.gz)"

prepare() {
  cd "$_dirname"
  patch -Np1 < "$srcdir/llvm-project-mlir-fix-rpath-flags.patch"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  # -fPIC fixes linking.
  export CXXFLAGS="${CXXFLAGS} -fcf-protection=none -fPIC"

  cmake -S "$_dirname" \
    -DCMAKE_BUILD_TYPE=Release \
    -DMLIR_MIOPEN_SQLITE_ENABLED=On \
    -DLLVM_TARGETS_TO_BUILD="X86;AMDGPU" \
    -DCMAKE_INSTALL_PREFIX='/opt/rocm' \
    -DBUILD_FAT_LIBMLIRMIOPEN=1

  make
}

package() {
  make DESTDIR="$pkgdir/" install

  cd "$_dirname"
  install -Dm644 mlir/LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
