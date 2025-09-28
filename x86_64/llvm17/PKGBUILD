# Maintainer: Stefan Wimmer <info@stefanwimmer128.xyz>
# Contributor: Daniele Basso
# Contributor: Lancelot Owczarczak <lancelot@owczarczak.fr>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>

pkgname=('llvm17' 'llvm17-libs')
pkgver=17.0.6
pkgrel=2
arch=('x86_64')
url="https://llvm.org/"
license=('custom:Apache 2.0 with LLVM Exception')
makedepends=('cmake' 'ninja' 'zlib' 'zstd' 'libffi' 'libedit' 'ncurses'
             'libxml2' 'python' 'python-build' 'python-setuptools' 'python-wheel')
checkdepends=('python-psutil')
options=('staticlibs' '!lto') # tools/llvm-shlib/typeids.test fails with LTO
_source_base=https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver
source=($_source_base/llvm-$pkgver.src.tar.xz
        $_source_base/cmake-$pkgver.src.tar.xz
        $_source_base/third-party-$pkgver.src.tar.xz)
b2sums=('2d1305a7b059d6b425cbe560bc5b5764934bd690206ace1f50ab317972c5a380768a86f3542b27be299c12ab356099fe80876a57978c41d9131ec2a2e038f42c'
        'f95c1c951ba7bd943931bb18c8dc23ef0b3c20ee3dd254d458ab7a3339097fc0f9e11c3b892c352e3f5f131014265a6bb116f56c9ebd78408f05158a90f51d6b'
        '98e7525ae1106bce37809b77bf23a75b7e3ea14fa31342bfe50e8da3532952254be2424aba7241850e8b7d97dc55c0da1162d31ae5485774b5902d521da449bd')

# Utilizing LLVM_DISTRIBUTION_COMPONENTS to avoid
# installing static libraries; inspired by Gentoo
_get_distribution_components() {
  local target
  ninja -C build -t targets | grep -Po 'install-\K.*(?=-stripped:)' | while read -r target; do
    case $target in
      llvm-libraries|distribution)
        continue
        ;;
      # shared libraries
      LLVM|LLVMgold)
        ;;
      # libraries needed for clang-tblgen
      LLVMDemangle|LLVMSupport|LLVMTableGen)
        ;;
      # exclude static libraries
      LLVM*)
        continue
        ;;
      # exclude llvm-exegesis (doesn't seem useful without libpfm)
      llvm-exegesis)
        continue
        ;;
      # testing libraries
      LLVMTestingAnnotations|LLVMTestingSupport)
        ;;
    esac
    echo $target
  done
}

prepare() {
  rename -v -- "-$pkgver.src" '' {cmake,third-party}-$pkgver.src

  cd "llvm-$pkgver.src" || exit

  # https://aur.archlinux.org/packages/llvm17#comment-1039830
  # https://gcc.gnu.org/gcc-15/porting_to.html#header-dep-changes
  sed -i '29i #include <cstdint>' include/llvm/ADT/SmallVector.h
  sed -i '19i #include <cstdint>' lib/Target/AMDGPU/MCTargetDesc/AMDGPUMCTargetDesc.h
  sed -i '18i #include <cstdint>' lib/Target/X86/MCTargetDesc/X86MCTargetDesc.h
}

build() {
  cd llvm-$pkgver.src

  # Build only minimal debug info to reduce size
  CFLAGS=${CFLAGS/-g /-g1 }
  CXXFLAGS=${CXXFLAGS/-g /-g1 }

  local cmake_args=(
    -G Ninja
    -DCMAKE_BUILD_TYPE=Release
    -DCMAKE_INSTALL_PREFIX=/usr/lib/llvm17
    -DCMAKE_INSTALL_DOCDIR=share/doc
    -DCMAKE_SKIP_RPATH=ON
    -DLLVM_BINUTILS_INCDIR=/usr/include
    -DLLVM_BUILD_DOCS=ON
    -DLLVM_BUILD_LLVM_DYLIB=ON
    -DLLVM_BUILD_TESTS=ON
    -DLLVM_ENABLE_BINDINGS=OFF
    -DLLVM_ENABLE_FFI=ON
    -DLLVM_ENABLE_RTTI=ON
    -DLLVM_ENABLE_SPHINX=OFF
    -DLLVM_HOST_TRIPLE=$CHOST
    -DLLVM_INCLUDE_BENCHMARKS=OFF
    -DLLVM_INSTALL_UTILS=ON
    -DLLVM_LINK_LLVM_DYLIB=ON
    -DLLVM_USE_PERF=ON
    -DLLVM_INSTALL_GTEST=ON
    -DSPHINX_WARNINGS_AS_ERRORS=OFF
  )

  cmake "${cmake_args[@]}" -B build
  local distribution_components=$(_get_distribution_components | paste -sd\;)
  test -n "$distribution_components"
  cmake_args+=(-DLLVM_DISTRIBUTION_COMPONENTS="$distribution_components")

  cmake "${cmake_args[@]}" -B build
  ninja -C build

  cd utils/lit
  python -m build --wheel --no-isolation
}

check() {
  cd llvm-$pkgver.src/build
  LD_LIBRARY_PATH=$PWD/lib ninja check
}

package_llvm17() {
  pkgdesc="Compiler infrastructure (LLVM 17)"
  depends=('llvm17-libs' 'perl')

  cd llvm-$pkgver.src/build

  DESTDIR="$pkgdir" ninja install-distribution

  # The runtime libraries go into llvm17-libs
  mv -f "$pkgdir"/usr/lib/llvm17/lib/libLLVM-{17,$pkgver}.so "$srcdir/"
  mv -f "$pkgdir"/usr/lib/llvm17/lib/LLVMgold.so "$srcdir/"

  # Create versioned symlinks from /usr/bin/ to /usr/lib/llvm17/bin/
  install -d "$pkgdir/usr/bin"
  local _binary
  for _binary in "$pkgdir"/usr/lib/llvm17/bin/*; do
    local _basename=${_binary##*/}
    ln -s ../lib/llvm17/bin/$_basename "$pkgdir/usr/bin/$_basename-17"
  done

  install -Dm644 ../LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_llvm17-libs() {
  pkgdesc="LLVM 17 runtime libraries"
  depends=('gcc-libs' 'zlib' 'libffi' 'libedit' 'ncurses' 'libxml2')

  install -d "$pkgdir/usr/lib/llvm17/lib"
  cp -P "$srcdir"/libLLVM-{17,$pkgver}.so "$pkgdir/usr/lib/"
  ln -s ../../libLLVM-17.so "$pkgdir/usr/lib/llvm17/lib/libLLVM-17.so"
  ln -s ../../libLLVM-17.so "$pkgdir/usr/lib/llvm17/lib/libLLVM-$pkgver.so"
  cp -P "$srcdir"/LLVMgold.so "$pkgdir/usr/lib/llvm17/lib/"

  install -Dm644 "$srcdir/llvm-$pkgver.src/LICENSE.TXT" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
# vim:set ts=2 sw=2 et:
