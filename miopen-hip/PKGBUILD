# Maintainer: acxz <akashpatel at yahoo dot com>

pkgname=miopen-hip
pkgver=3.8.0
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
sha256sums=('612b30d4a967bf18c7fa7aa3ef12ed558314ed04cee2775b842bf6a96cd7276f')

build() {
  CXXFLAGS="$CXXFLAGS -DHALF_ENABLE_F16C_INTRINSICS=0 -isystem /opt/rocm/llvm/lib/clang/11.0.0" \
  CPPFLAGS="$CPPFLAGS -DHALF_ENABLE_F16C_INTRINSICS=0 -isystem /opt/rocm/llvm/lib/clang/11.0.0" \
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -S "MIOpen-rocm-$pkgver" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DMIOPEN_BACKEND=HIP \
        -DMIOPEN_HIP_COMPILER=/opt/rocm/llvm/bin/clang++ \
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
