# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocprim
pkgver=5.1.3
pkgrel=1
pkgdesc='Header-only library providing HIP parallel primitives'
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocPRIM"
license=('MIT')
depends=('hip')
makedepends=('cmake' 'rocm-cmake' 'git')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('b5a08d2e76388bd1ffa6c946009928fe95de846ab6b65a6475998070c0cf6dc1')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-5.1.x/docs/markdown/clang_options.md

  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF \
        -DBUILD_BENCHMARK=OFF
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
