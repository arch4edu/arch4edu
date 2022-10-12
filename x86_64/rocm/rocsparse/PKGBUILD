# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=5.3.0
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocsparse.readthedocs.io/en/master/'
license=('MIT')
depends=('hip' 'rocprim')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('521ca0e7b52f26edbff8507eb1479dc26019f456756d884d7b8b192c3ea518e8')
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
    -Drocprim_DIR=/opt/rocm/rocprim/rocprim/lib/cmake/rocprim \
    -DBUILD_CLIENTS_SAMPLES=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo '/opt/rocm/rocsparse/lib' > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
