# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocalution
_pkgver=3.1
pkgver="$_pkgver.0"
pkgrel=3
pkgdesc="Next generation library for iterative sparse solvers for ROCm platform."
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocALUTION"
license=('custom:NCSAOSL')
depends=('hcc' 'hip' 'rocsparse' 'rocblas' 'rocprim' 'comgr')
makedepends=('cmake' "hcc>=$pkgver" "hip>=$pkgver" "rocsparse>=$pkgver" "rocblas>=$pkgver" "rocprim>=$pkgver" "comgr>=$pkgver" 'python2' 'rocminfo')
source=("https://github.com/ROCmSoftwarePlatform/rocALUTION/archive/rocm-$_pkgver.tar.gz")
sha256sums=('45c96916f915fcacab3a94f111912e9511167977678603f3c7253053eeec6513')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  # Tensile library needs python to be python2
  export PATH="$srcdir:$PATH"
  [[ -e "$srcdir/python" ]] || ln -s /usr/bin/python2 "$srcdir/python"

  # fix broken build with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  # compile with HCC
  export CXX="/opt/rocm/hcc/bin/hcc"

#        -ROCBLAS_DIR=/opt/rocm/rocblas/lib/cmake/rocblas \
  # TODO: fix librocalution.so, it contains references to $srcdir
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocalution \
        -ROCSPARSE_DIR=/opt/rocm/rocsparse/lib/cmake/rocsparse \
        -Dhip_DIR=/opt/rocm/hip/lib/cmake/hip \
        -Dhcc_DIR=/opt/rocm/hcc/lib/cmake/hcc \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF \
        "$srcdir/rocALUTION-rocm-$_pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocalution.conf"
/opt/rocm/rocalution/lib
EOF
}
