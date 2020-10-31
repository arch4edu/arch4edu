# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=hipcub
pkgver=3.9.0
pkgrel=1
pkgdesc='Header-only library on top of rocPRIM or CUB'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#hipcub'
license=('custom')
depends=('rocprim')
makedepends=('cmake' 'git' 'hip-rocclr')
_git='https://github.com/ROCmSoftwarePlatform/hipCUB'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('c46995f9f18733ec18e370c21d7c0d6ac719e8e9d3254c6303a20ba90831e12e')
_dirname="$(basename $_git)-$(basename "${source[0]}" ".tar.gz")"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr
}

package() {
  DESTDIR="$pkgdir" make install
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
