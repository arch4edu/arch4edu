# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=hipcub
pkgver=5.4.0
pkgrel=1
pkgdesc='Header-only library on top of rocPRIM or CUB'
arch=('x86_64')
url='https://hipcub.readthedocs.io/en/latest/'
license=('custom')
depends=('rocprim' 'hip')
makedepends=('rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/hipCUB'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('78db2c2ea466a4c5d84beedc000ae934f6d0ff1793eae90bb8d02b2dbff8932c')
_dirname="$(basename $_git)-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html

  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -S "$_dirname" \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
