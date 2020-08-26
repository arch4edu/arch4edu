# Maintainer: acxz <akashpatel at yahoo dot com>

pkgname=miopen-hip
pkgver=3.7.0
pkgrel=1
pkgdesc="AMD's Machine Intelligence Library (HIP backend)"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpen"
license=('custom:NCSAOSL')
depends=('rocblas' 'boost' 'llvm-amdgpu' 'rocm-clang-ocl' 'hip')
makedepends=('cmake' 'rocm-cmake' 'half' 'miopengemm' 'clang' 'rocminfo')
provides=('miopen')
conflicts=('miopen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('f6a6ddd8d39bb76b7f7d91e68ade3b45e0201181145658c43b967065a354b103')

build() {
  CXXFLAGS="$CXXFLAGS -DHALF_ENABLE_F16C_INTRINSICS=0 -isystem /opt/rocm/llvm/lib/clang/11.0.0" \
  CPPFLAGS="$CPPFLAGS -DHALF_ENABLE_F16C_INTRINSICS=0 -isystem /opt/rocm/llvm/lib/clang/11.0.0" \
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -S "MIOpen-rocm-$pkgver" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
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
