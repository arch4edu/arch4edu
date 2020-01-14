# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>

pkgname=('llvm8' 'llvm8-libs')
pkgver=8.0.1
pkgrel=1
arch=('x86_64')
url="https://llvm.org/"
license=('custom:University of Illinois/NCSA Open Source License')
makedepends=('cmake' 'ninja' 'libffi' 'libedit' 'ncurses' 'libxml2'
             'python-sphinx' 'python-recommonmark' 'python-setuptools')
options=('staticlibs')
source=(https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/llvm-$pkgver.src.tar.xz)
sha256sums=('44787a6d02f7140f145e2250d56c9f849334e11f9ae379827510ed72f12b75e7')

prepare() {
  cd "$srcdir/llvm-$pkgver.src"
  mkdir build
}

build() {
  cd "$srcdir/llvm-$pkgver.src/build"

  cmake .. -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DLLVM_HOST_TRIPLE=$CHOST \
    -DLLVM_BUILD_LLVM_DYLIB=ON \
    -DLLVM_LINK_LLVM_DYLIB=ON \
    -DLLVM_INSTALL_UTILS=ON \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_ENABLE_FFI=ON \
    -DLLVM_BUILD_TESTS=ON \
    -DLLVM_BUILD_DOCS=ON \
    -DLLVM_ENABLE_SPHINX=ON \
    -DLLVM_ENABLE_DOXYGEN=OFF \
    -DSPHINX_WARNINGS_AS_ERRORS=OFF \
    -DFFI_INCLUDE_DIR=$(pkg-config --variable=includedir libffi) \
    -DLLVM_BINUTILS_INCDIR=/usr/include
  ninja
}

check() {
  cd "$srcdir/llvm-$pkgver.src/build"
  ninja check
}

package_llvm8() {
  pkgdesc="Collection of modular and reusable compiler and toolchain technologies"
  depends=('llvm8-libs' 'perl')
  optdepends=('python-setuptools: for using lit (LLVM Integrated Tester)')
  conflicts=('llvm')

  cd "$srcdir/llvm-$pkgver.src/build"

  DESTDIR="$pkgdir" ninja install

  # Include lit for running lit-based tests in other projects
  pushd ../utils/lit
  python3 setup.py install --root="$pkgdir" -O1
  popd

  # The runtime libraries go into llvm8-libs
  mv -f "$pkgdir"/usr/lib/lib{LLVM-*.so,LTO.so.*} "$srcdir"

  # Remove files which conflict with llvm-libs
  rm "$pkgdir"/usr/lib/{LLVMgold,lib{LLVM,LTO}}.so

  install -Dm644 ../LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_llvm8-libs() {
  pkgdesc="LLVM 8 runtime libraries"
  depends=('gcc-libs' 'zlib' 'libffi' 'libedit' 'ncurses' 'libxml2')

  install -d "$pkgdir/usr/lib"
  cp -P "$srcdir"/lib{LLVM-*.so,LTO.so.*} "$pkgdir/usr/lib/"

  install -Dm644 "$srcdir/llvm-$pkgver.src/LICENSE.TXT" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
