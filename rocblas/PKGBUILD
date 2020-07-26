# Maintainer: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
pkgver=3.5.0
pkgrel=2
pkgdesc='Next generation BLAS implementation for ROCm platform'
arch=('x86_64')
url='https://rocblas.readthedocs.io/en/latest'
license=('MIT')
depends=('hip-rocclr' 'openmp')
makedepends=('cmake' 'python' 'python-virtualenv' 'python-pyaml' 'perl-file-which' 'rocm-cmake' 'llvm-amdgpu')
_rocblas='https://github.com/ROCmSoftwarePlatform/rocBLAS'
_tensile='https://github.com/ROCmSoftwarePlatform/Tensile'
source=("$pkgname-$pkgver.tar.gz::$_rocblas/archive/rocm-$pkgver.tar.gz"
        "rocm-tensile-$pkgver.tar.gz::$_tensile/archive/rocm-$pkgver.tar.gz")
sha256sums=('8560fabef7f13e8d67da997de2295399f6ec595edfd77e452978c140d5f936f0'
            '71eb3eed6625b08a4cedb539dd9b596e3d4cc82a1a8063d37d94c0765b6f8257')
options=(!strip)

prepare() {
  cd "$srcdir/Tensile-rocm-$pkgver"
  # override __hcc_workweek__
  # https://github.com/rocm-arch/rocm-arch/issues/68#issuecomment-604272120
  sed -i 's/__hcc_workweek__/99999/g' $(grep __hcc_workweek__ . -rIl)
}

build() {
  # fix broken build with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_PREFIX_PATH=/opt/rocm/llvm/lib/cmake/llvm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_WITH_TENSILE=ON \
        -DTensile_TEST_LOCAL_PATH="$srcdir/Tensile-rocm-$pkgver" \
        -DTensile_COMPILER=hipcc \
        -DTensile_ARCHITECTURE=all \
        -DTensile_LOGIC=asm_full \
        -DBUILD_CLIENTS_TESTS=OFF \
        -DBUILD_CLIENTS_BENCHMARKS=OFF \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_TESTING=OFF \
        "$srcdir/rocBLAS-rocm-$pkgver"

  # Fix for latest llvm
  sed -i 's/Impl::inputOne(io, key, \*value)/Impl::inputOne(io, key.str(), \*value)/g' \
    $srcdir/build/virtualenv/lib/python*/site-packages/Tensile/Source/lib/include/Tensile/llvm/YAML.hpp

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocblas.conf" << EOF
/opt/rocm/rocblas/lib
EOF
  install -Dm644 "$srcdir/rocBLAS-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
