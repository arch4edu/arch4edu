# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocprim
pkgver=5.4.1
pkgrel=1
pkgdesc='Header-only library providing HIP parallel primitives'
arch=('x86_64')
url='https://github.com/ROCmSoftwarePlatform/rocPRIM'
license=('MIT')
depends=('hip')
makedepends=('rocm-cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('3a2e09eb5b65114444feed545c03fbf766af33ace1f14467d4190d63c688ca61')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html

  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -S "$_dirname" \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
