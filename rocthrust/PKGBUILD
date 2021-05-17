# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocthrust
pkgver=4.2.0
pkgrel=1
pkgdesc='Port of the Thrust parallel algorithm library atop HIP/ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocthrust'
license=('Apache')
depends=('hip-rocclr' 'rocprim')
makedepends=('cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocThrust'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('da2b6c831c26c26058218b0c5b7b2e43fd7f0dac3b2e3a8e39a839145592c727')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-4.2.x/docs/markdown/clang_options.md
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF
}

package() {
  DESTDIR="$pkgdir" make install
}
