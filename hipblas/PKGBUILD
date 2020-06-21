# Maintainer: Markus Näther <naether.markus@gmail.com>
pkgname=hipblas
pkgver=3.5.0
pkgrel=1
pkgdesc='ROCm BLAS marshalling library'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#hipblas'
license=('MIT')
depends=('hip-rocclr' 'rocblas' 'rocsolver')
makedepends=('cmake' 'rocminfo')
_git='https://github.com/ROCmSoftwarePlatform/hipBLAS'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('d451da80beb048767da71a090afceed2e111d01b3e95a7044deada5054d6e7b1')

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF \
        "$srcdir/hipBLAS-rocm-$pkgver"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipblas.conf" <<EOF
/opt/rocm/hipblas/lib
EOF
  install -Dm644 "$srcdir/hipBLAS-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
