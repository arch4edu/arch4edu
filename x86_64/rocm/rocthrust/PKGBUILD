# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocthrust
pkgver=5.2.3
pkgrel=2
pkgdesc='Port of the Thrust parallel algorithm library atop HIP/ROCm'
arch=('x86_64')
url='https://docs.amd.com/bundle/rocTHRUST_API_Guide/page/index.html'
license=('Apache')
depends=('hip' 'rocprim')
makedepends=('cmake' 'rocm-cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocThrust'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('0f5ef39c5faab31eb34b48391d58096463969c133ca7ed09ab4e43caa5461b29')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -S "$_dirname" \
    -B build \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
    -DBUILD_TEST=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
