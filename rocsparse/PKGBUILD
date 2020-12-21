# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=4.0.0
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocsparse'
license=('MIT')
depends=('hip-rocclr' 'rocprim')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('2b41bc6623d204ad7f351a902810f34cd32b762d1bf59081dbb00f83e689a794')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Drocprim_DIR=/opt/rocm/rocprim/rocprim/lib/cmake/rocprim \
        -DBUILD_CLIENTS_SAMPLES=OFF
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocsparse.conf" <<EOF
/opt/rocm/rocsparse/lib
EOF
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
