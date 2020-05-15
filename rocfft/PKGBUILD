# Maintainer: Jakub Okoński <jakub@okonski.org>
# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=rocfft
_pkgver=3.3.0
pkgver="$_pkgver"
pkgrel=1
pkgdesc="Next generation FFT implementation for ROCm"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocfft"
license=('MIT')
depends=('boost' 'fftw')
makedepends=("hcc>=$pkgver" 'cmake')
source=("https://github.com/ROCmSoftwarePlatform/rocFFT/archive/rocm-$_pkgver.tar.gz")
sha256sums=('bbbafcac891ff237c67a3a8fe6e842880ad3c8753b200ecb11f23173ac737e1c')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  # build broken with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  # compile with HCC
  export CXX="/opt/rocm/hcc/bin/hcc"

  cmake -DCMAKE_BUILD_TYPE=Release \
        "$srcdir/rocFFT-rocm-$_pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocfft.conf"
/opt/rocm/rocfft/lib
EOF
}
