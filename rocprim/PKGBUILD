# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocprim
pkgver=3.3.0
pkgrel=2
pkgdesc="ROCm Parallel Primitives"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocPRIM"
license=('custom:NCSAOSL')
depends=('hcc' 'hip')
makedepends=('cmake' 'hcc' 'python2' 'rocminfo' 'comgr')
source=("https://github.com/ROCmSoftwarePlatform/rocPRIM/archive/rocm-$pkgver.tar.gz")
sha256sums=('506c014bd573ba1473230087ca30394ca6ef34f58e7248a858342b2173009000')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  # fix broken build with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  # compile with HCC
  export CXX="/opt/rocm/hcc/bin/hcc"

  # TODO: fix librocprim.so, it contains references to $srcdir
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocprim \
        -DBUILD_TEST=OFF \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        "$srcdir/rocPRIM-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocprim.conf"
/opt/rocm/rocprim/lib
EOF
}
