# Maintainer: Jakub Okoński <jakub@okonski.org>
# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=rocfft
pkgver=3.5.0
pkgrel=1
pkgdesc='Next generation FFT implementation for ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocfft'
license=('MIT')
depends=('hip-rocclr')
makedepends=('cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocFFT'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('629f02cfecb7de5ad2517b6a8aac6ed4de60d3a9c620413c4d9db46081ac2c88')

build() {
  mkdir -p build
  cd build

  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_CLIENTS_RIDER=OFF \
        -DBUILD_CLIENTS_TESTS=OFF \
        "$srcdir/rocFFT-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocfft.conf" << EOF
/opt/rocm/rocfft/lib
EOF
  install -Dm644 "$srcdir/rocFFT-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
