# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=rocfft
pkgver=5.4.1
pkgrel=1
pkgdesc='Next generation FFT implementation for ROCm'
arch=('x86_64')
url='https://rocfft.readthedocs.io/en/latest/library.html'
license=('MIT')
depends=('hip' 'python')
makedepends=('rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocFFT'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('b2383cb6dfac285bae37733356dbd0f56b008f14db4b5a05bea8d28624cccffa')
options=(!lto)
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/rocfft.conf"

  install -Dm644 "$srcdir/$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
