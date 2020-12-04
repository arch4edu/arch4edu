# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocprim
pkgver=3.10.0
pkgrel=1
pkgdesc='Header-only library providing HIP parallel primitives'
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocPRIM"
license=('MIT')
depends=('hip-rocclr')
makedepends=('cmake' 'git')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('b406956b27d1c06b749e991a250d4ad3eb26e20c6bebf121e2ca6051597b4fa4')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
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
