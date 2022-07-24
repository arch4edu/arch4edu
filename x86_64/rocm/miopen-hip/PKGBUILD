# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=miopen-hip
pkgver=5.2.1
pkgrel=1
pkgdesc="AMD's Machine Intelligence Library (HIP backend)"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpen"
license=('MIT')
depends=('rocblas' 'rocm-clang-ocl' 'hip' 'rocm-llvm-mlir')
makedepends=('cmake' 'rocm-cmake' 'miopengemm' 'sqlite' 'boost>=1.78')
provides=('miopen')
conflicts=('miopen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
       "https://github.com/ROCmSoftwarePlatform/MIOpen/commit/9ae2418adf767794e9475274a4cf90e418f00a58.patch")
sha256sums=('0977a8876d41bbd2fa268341c93892f35878d7efc1711194ad87582f877ff500'
            '329970d0f9b63b1d814a7256def2b2167ce5cb0e56a6ea037c9c40b225b8cd9f')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
  cd "$_dirname"

  # -fcf-protection is not supported by HIP, see
  # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-5.1.x/docs/markdown/clang_options.md
  # -fPIC fixes linking errors.
  export CC=/opt/rocm/llvm/bin/clang
  export CXX=/opt/rocm/llvm/bin/clang++
  export CXXFLAGS="${CXXFLAGS} -fcf-protection=none -fPIC"

  # We can use the system SQLite and Boost
  msg2 "Building dependencies"
  sed -i 's|^sqlite|#\0|' {,min-}requirements.txt
  sed -i 's|^boost|#\0|' {,min-}requirements.txt
  sed -i 's|^ROCmSoftwarePlatform/llvm-project-mlir|#\0|' {,min-}requirements.txt
  ./install_deps.cmake --minimum --prefix "$srcdir/deps"

  msg2 "Patching files"
  for p in $srcdir/*.patch ; do
    patch -p1 < $p
  done
}

build() {
  cd "$_dirname"

  # -fcf-protection is not supported by HIP, see
  # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-5.1.x/docs/markdown/clang_options.md
  # -fPIC fixes linking errors with boost.
  export CC=/opt/rocm/llvm/bin/clang
  export CXX=/opt/rocm/llvm/bin/clang++
  export CXXFLAGS="${CXXFLAGS} -fcf-protection=none -fPIC"

  cmake -B build -Wno-dev \
        -DMIOPEN_BACKEND=HIP \
        -DCMAKE_PREFIX_PATH="$srcdir/deps" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C "$_dirname/build" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/miopen.conf"
/opt/rocm/miopen/lib
EOF

  install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
