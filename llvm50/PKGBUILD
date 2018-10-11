# $Id$
# Maintainer: Solomon Choina <shlomochoina@gmail.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Sebastian Nowicki <sebnow@gmail.com>
# Contributor: Devin Cofer <ranguvar{AT]archlinux[DOT}us>
# Contributor: Tobias Kieslich <tobias@justdreams.de>
# Contributor: Geoffroy Carrier <geoffroy.carrier@aur.archlinux.org>
# Contributor: Tomas Lindquist Olsen <tomas@famolsen.dk>
# Contributor: Roberto Alsina <ralsina@kde.org>
# Contributor: Gerardo Exequiel Pozzi <vmlinuz386@yahoo.com.ar>
# Contributor: Ruben Van Boxem <vanboxem.ruben@gmail.com>

pkgname=('llvm50' 'llvm50-libs' 'clang50')
pkgver=5.0.2
pkgrel=5
_prefix="/usr/lib/llvm-5.0"
arch=('i686' 'x86_64')
url="http://llvm.org/"
license=('custom:University of Illinois/NCSA Open Source License')
makedepends=('cmake' 'libffi' 'python2' 'python-sphinx' 'libedit' 'swig' 'icu59')
makedepends_x86_64=('gcc-multilib')
options=('staticlibs')
source=(https://releases.llvm.org/$pkgver/llvm-$pkgver.src.tar.xz
        https://releases.llvm.org/$pkgver/cfe-$pkgver.src.tar.xz
        https://releases.llvm.org/$pkgver/compiler-rt-$pkgver.src.tar.xz
        0001-GCC-compatibility-Ignore-the-fno-plt-flag.patch
        0002-Enable-SSP-and-PIE-by-default.patch
        disable-llvm-symbolizer-test.patch
        gcc-build-fix.patch
        glibc.diff)
sha256sums=('d522eda97835a9c75f0b88ddc81437e5edbb87dc2740686cb8647763855c2b3c'
            'fa9ce9724abdb68f166deea0af1f71ca0dfa9af8f7e1261f2cae63c280282800'
            '3efe9ddf3f69e0c0a45cde57ee93911f36f3ab5f2a7f6ab8c8efb3db9b24ed46'
            'a1ba7fb859ac157c4b4342435cd656e29b1e1d9bddcb8ae0158a91c0a8ba6203'
            '186f2d10b013395f2dd6e1fd3baf4961a2e40c403f115517c9b253682934f50f'
            '6fff47ab5ede79d45fe64bb4903b7dfc27212a38e6cd5d01e60ebd24b7557359'
            '2e707016fef45434f48c06326c968c11e08445eeb37c53cf55ac592c08262577'
            '4f9e747b4c79f1357ae885f81ef1115e7144ba553dabd0484e87bc5ea69cb0b4')

prepare() {
  cd "$srcdir/llvm-$pkgver.src"
  mkdir build

  mv "$srcdir/cfe-$pkgver.src" tools/clang
  mv "$srcdir/compiler-rt-$pkgver.src" projects/compiler-rt

  # Disable test that fails when compiled as PIE
  # https://bugs.llvm.org/show_bug.cgi?id=31870
  patch -Np1 <../disable-llvm-symbolizer-test.patch

  # Enable SSP and PIE by default
  patch -Np1 -d tools/clang <../0001-GCC-compatibility-Ignore-the-fno-plt-flag.patch
  patch -Np1 -d tools/clang <../0002-Enable-SSP-and-PIE-by-default.patch
  patch -Np1 -i ../gcc-build-fix.patch
  patch -Np1 -i ../glibc.diff

}

build() {
  cd "$srcdir/llvm-$pkgver.src/build"

  cmake .. -G 'Unix Makefiles' \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="${_prefix}" \
    -DLLVM_BUILD_LLVM_DYLIB=ON \
    -DLLVM_LINK_LLVM_DYLIB=ON \
    -DLLVM_INSTALL_UTILS=ON \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_ENABLE_FFI=ON \
    -DLLVM_BUILD_TESTS=ON \
    -DLLVM_ENABLE_DOXYGEN=OFF \
    -DCLANG_INSTALL_SCANBUILD=OFF \
    -DCLANG_INSTALL_SCANVIEW=OFF \
    -DFFI_INCLUDE_DIR=$(pkg-config --variable=includedir libffi) \
    -DLLVM_BINUTILS_INCDIR=/usr/include 

  make all
  cd docs
  make ocaml_doc
  cd ..

  # Disable automatic installation of components that go into subpackages
  sed -i '/clang\/cmake_install.cmake/d' tools/cmake_install.cmake
  sed -i '/extra\/cmake_install.cmake/d' tools/clang/tools/cmake_install.cmake
  sed -i '/compiler-rt\/cmake_install.cmake/d' projects/cmake_install.cmake
}

check() {
  cd "$srcdir/llvm-$pkgver.src/build"
  #make check-{llvm,clang}
}

package_llvm50() {
  pkgdesc="Low Level Virtual Machine"
  depends=('llvm50-libs' 'perl')
  
  cd "$srcdir/llvm-$pkgver.src"

  make -C build DESTDIR="$pkgdir" install

  # The runtime libraries go into llvm-libs
  mv -f "${pkgdir}${_prefix}"/lib/lib{LLVM,LTO}*.so* "$srcdir"
  mv -f "${pkgdir}${_prefix}"/lib/LLVMgold.so "$srcdir"
  
  #remove ocaml files
  rm -rf $pkgdir/usr/lib/ocaml
  install -Dm644 LICENSE.TXT "${pkgdir}${_prefix}/share/licenses/llvm/LICENSE"

  # add symbolic links in /usr/bin
  mkdir -p "$pkgdir/usr/bin"
  cd "${pkgdir}${_prefix}"/bin
  for f in *; do
    ln -s "${_prefix}/bin/$f" "$pkgdir/usr/bin/${f%-5.0}-5.0"
  done
}

package_llvm50-libs() {
  pkgdesc="Low Level Virtual Machine (runtime libraries)"
  depends=('gcc-libs' 'zlib' 'libffi' 'libedit' 'ncurses')

  install -d "${pkgdir}${_prefix}/lib"
  cp -P \
    "$srcdir"/lib{LLVM,LTO}*.so* \
    "$srcdir"/LLVMgold.so \
    "${pkgdir}${_prefix}/lib/"

  install -d $pkgdir/usr/lib
  cd ${pkgdir}/usr/lib/
  ln -s llvm-5.0/lib/lib{LLVM,LTO}*.so* ./
  rm $pkgdir/usr/lib/lib{LLVM,LTO}.so

  install -Dm644 "$srcdir/llvm-$pkgver.src/LICENSE.TXT" \
    "${pkgdir}${_prefix}/share/licenses/llvm-libs/LICENSE"
}

package_clang50() {
  pkgdesc="C language family frontend for LLVM"
  url="http://clang.llvm.org/"
  depends=('llvm50-libs' 'gcc' 'libxml2')
  optdepends=('openmp: OpenMP support in clang with -fopenmp')

  cd "$srcdir/llvm-$pkgver.src"

  make -C build/tools/clang DESTDIR="$pkgdir" install
  make -C build/projects/compiler-rt DESTDIR="$pkgdir" install
  install -Dm644 tools/clang/LICENSE.TXT \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    
  # add symbolic links in /usr/bin
  mkdir -p "$pkgdir/usr/bin"
  cd "${pkgdir}${_prefix}"/bin
  for f in *; do
    ln -f -s "${_prefix}/bin/$f" "$pkgdir/usr/bin/${f%-5.0}-5.0"
  done
  
  cd ${pkgdir}${_prefix}/lib
  ln -s *clang*.*so* ${pkgdir}/usr/lib
  rm ${pkgdir}/usr/lib/libclang.so
}
# vim:set ts=2 sw=2 et:
