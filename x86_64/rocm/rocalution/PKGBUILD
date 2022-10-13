# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocalution
pkgver=5.3.0
pkgrel=1
pkgdesc='Next generation library for iterative sparse solvers for ROCm platform'
arch=('x86_64')
url='https://rocalution.readthedocs.io/en/master'
license=('MIT')
depends=('hip' 'rocsparse' 'rocblas' 'rocprim' 'rocrand' 'openmp')
makedepends=('rocm-cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocALUTION'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('f623449789a5c9c9137ae51d4dbbee5c6940d8813826629cb4b7e84f07fab494')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DROCM_PATH=/opt/rocm
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/rocalution.conf"

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
