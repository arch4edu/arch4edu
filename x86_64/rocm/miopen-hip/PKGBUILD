# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=miopen-hip
pkgver=5.3.0
pkgrel=1
pkgdesc="AMD's Machine Intelligence Library (HIP backend)"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpen"
license=('MIT')
depends=('rocblas' 'rocm-clang-ocl' 'hip' 'rocm-llvm-mlir')
makedepends=('rocm-cmake' 'miopengemm' 'sqlite' 'boost')
provides=('miopen')
conflicts=('miopen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('c5819f593d71beeda2eb24b89182912240cc40f83b2b8f9de695a8e230aa4ea6')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
  cd "$_dirname"

  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Appendix_A.html
  # -fPIC fixes linking errors.
  export CC=/opt/rocm/llvm/bin/clang
  export CXX=/opt/rocm/llvm/bin/clang++
  export CXXFLAGS="${CXXFLAGS} -fcf-protection=none -fPIC"

  # We can use the system SQLite and Boost
  sed -i 's|^sqlite|#\0|' {,min-}requirements.txt
  sed -i 's|^boost|#\0|' {,min-}requirements.txt
  sed -i 's|^ROCmSoftwarePlatform/llvm-project-mlir|#\0|' {,min-}requirements.txt
  ./install_deps.cmake --minimum --prefix "$srcdir/deps"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Appendix_A.html
  # -fPIC fixes linking errors with boost.
  export CC=/opt/rocm/llvm/bin/clang
  export CXX=/opt/rocm/llvm/bin/clang++
  export CXXFLAGS="${CXXFLAGS} -fcf-protection=none -fPIC"

  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DMIOPEN_BACKEND=HIP \
    -DCMAKE_PREFIX_PATH="$srcdir/deps" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo '/opt/rocm/miopen/lib' > 'miopen.conf'
  install -Dm644 "miopen.conf" "$pkgdir/etc/ld.so.conf.d/miopen.conf"

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
