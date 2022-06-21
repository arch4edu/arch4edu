# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=hipcub
pkgver=5.1.3
pkgrel=1
pkgdesc='Header-only library on top of rocPRIM or CUB'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#hipcub'
license=('custom')
depends=('rocprim')
makedepends=('cmake' 'rocm-cmake' 'git' 'hip')
_git='https://github.com/ROCmSoftwarePlatform/hipCUB'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('dc75640689b6a5e15dd3acea643266bdf114ea63efc60be8272f484cf8f04494')
_dirname="$(basename $_git)-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-5.1.x/docs/markdown/clang_options.md

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
