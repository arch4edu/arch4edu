# Maintainer: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
_pkgver=3.3.0
pkgver="$_pkgver"
pkgrel=3
pkgdesc="Next generation BLAS implementation for ROCm platform"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocBLAS"
license=('custom:NCSAOSL')
depends=('hcc' 'hip')
makedepends=('cmake' "hcc>=$pkgver" 'python' 'boost' "comgr>=$pkgver" 'rocminfo' 'hsa-ext-rocr')
source=("https://github.com/ROCmSoftwarePlatform/rocBLAS/archive/rocm-$_pkgver.tar.gz")
sha256sums=('aaa8f0479202bdbe94d2ec5655a76055656f743b0d36816501cb84a533084034')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  # fix broken build with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  # compile with HCC
  export CXX="/opt/rocm/hcc/bin/hcc"

  # TODO: fix librocblas.so, it contains references to $srcdir
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocblas \
        -HIP_DIR=/opt/rocm/hip/lib/cmake/hip \
        -hcc_DIR=/opt/rocm/hcc/lib/cmake/hcc \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        "$srcdir/rocBLAS-rocm-$_pkgver"

  # Fix for latest llvm
  sed -i 's/Impl::inputOne(io, key, \*value)/Impl::inputOne(io, key.str(), \*value)/g' \
    $srcdir/build/virtualenv/lib/python*/site-packages/Tensile/Source/lib/include/Tensile/llvm/YAML.hpp

  make -j 2
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocblas.conf"
/opt/rocm/rocblas/lib
EOF
}
