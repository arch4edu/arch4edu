# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocthrust
pkgver=3.3.0
pkgrel=3
pkgdesc="Port of the Thrust parallel algorithm library atop HIP/ROCm."
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocThrust"
license=('custom:NCSAOSL')
depends=('hcc' 'hip')
makedepends=('cmake' 'hcc' 'python2' 'rocminfo' 'comgr')
source=("https://github.com/ROCmSoftwarePlatform/rocThrust/archive/rocm-$pkgver.tar.gz")
sha256sums=('5782c9b96233b2050168381b3c2259baeb410b859f68c25b2d14110fb1bb726f')

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

  # TODO: fix librocthrust.so, it contains references to $srcdir
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocthrust \
        -DBUILD_TEST=OFF \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        "$srcdir/rocThrust-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocthrust.conf"
/opt/rocm/rocthrust/lib
EOF

  install -d "$pkgdir/opt/rocm/include"
  ln -s /opt/rocm/rocthrust/include/thrust "$pkgdir/opt/rocm/include"
}
