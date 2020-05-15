# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=hipsparse
pkgver=3.3.0
pkgrel=2
pkgdesc="ROCm SPARSE marshalling library."
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/hipSPARSE"
license=('custom:NCSAOSL')
depends=('hcc' 'hip')
makedepends=('cmake' "hcc>=$pkgver" "hip>=$pkgver" 'python' "rocprim>=$pkgver" "rocsparse>=$pkgver" "comgr>=$pkgver" 'rocminfo')
source=("https://github.com/ROCmSoftwarePlatform/hipSPARSE/archive/rocm-$pkgver.tar.gz")
sha256sums=('c69336071f56c857e969f0fdfbc351f75cc44ed2e3b854b4688675a9cafe4e22')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  # fix broken build with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  # compile with hipcc
  export CXX="/opt/rocm/hip/bin/hipcc"

  # TODO: fix librocsparse.so, it contains references to $srcdir
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hipsparse \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF \
        -Drocsparse_DIR=/opt/rocm/rocsparse/lib/cmake/rocsparse \
        "$srcdir/hipSPARSE-rocm-$pkgver"

  make
}

package() {
  cd "$srcdir/build"

  make install

  cp -r "$srcdir/build/opt" "$pkgdir/"

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/hipsparse.conf"
/opt/rocm/hipsparse/lib
EOF
}
