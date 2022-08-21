# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=hipcub
pkgver=5.2.3
pkgrel=1
pkgdesc='Header-only library on top of rocPRIM or CUB'
arch=('x86_64')
url='https://docs.amd.com/bundle/hipCUB-release-rocm-rel-5.2/page/introduction.html'
license=('custom')
depends=('rocprim')
makedepends=('cmake' 'rocm-cmake' 'git' 'hip')
_git='https://github.com/ROCmSoftwarePlatform/hipCUB'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('cab929f10c649f8fd76df989a16d0cd9301bc6aaad91cd2f84498c831378d559')
_dirname="$(basename $_git)-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html

  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr
}

package() {
  DESTDIR="$pkgdir" make install
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
