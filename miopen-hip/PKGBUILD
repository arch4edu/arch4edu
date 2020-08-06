# Maintainer: acxz <akashpatel at yahoo dot com>

pkgname=miopen-hip
pkgver=3.5.0
pkgrel=4
pkgdesc="AMD's Machine Intelligence Library (HIP backend)"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpen"
license=('custom:NCSAOSL')
depends=('rocblas' 'boost' 'llvm-amdgpu' 'rocm-clang-ocl' 'hip')
makedepends=('cmake' 'rocm-cmake' 'half' 'miopengemm' 'clang' 'rocminfo')
provides=('miopen')
conflicts=('miopen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('aa362e69c4dce7f5751f0ee04c745735ea5454c8101050e9b92cc60fa3c0fb82')

build() {
  CXXFLAGS="$CXXFLAGS -DHALF_ENABLE_F16C_INTRINSICS=0 -isystem /opt/rocm/llvm/lib/clang/11.0.0" \
  CPPFLAGS="$CPPFLAGS -DHALF_ENABLE_F16C_INTRINSICS=0 -isystem /opt/rocm/llvm/lib/clang/11.0.0" \
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -S "MIOpen-rocm-$pkgver" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/miopen \
        -DMIOPEN_BACKEND=HIP \
        -DHALF_INCLUDE_DIR=/usr/include/half \
        -DBoost_NO_BOOST_CMAKE=ON

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/miopen.conf"
/opt/rocm/miopen/lib
EOF
}
