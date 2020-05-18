# Maintainer: Jakub Okoński <jakub@okonski.org>
# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=rocfft
pkgver=3.3.0
pkgrel=1
pkgdesc='Next generation FFT implementation for ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocfft'
license=('MIT')
depends=('hip-hcc')
makedepends=('hcc' 'cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocFFT'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('bbbafcac891ff237c67a3a8fe6e842880ad3c8753b200ecb11f23173ac737e1c')

build() {
  mkdir -p build
  cd build

  # build broken with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  CXX=/opt/rocm/hcc/bin/hcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocfft \
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
