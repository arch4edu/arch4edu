# Maintainer: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
pkgver=4.0.0
pkgrel=1
pkgdesc='Next generation BLAS implementation for ROCm platform'
arch=('x86_64')
url='https://rocblas.readthedocs.io/en/latest'
license=('MIT')
depends=('hip-rocclr' 'openmp')
makedepends=('cmake' 'git' 'python' 'python-virtualenv' 'python-pyaml'
             'perl-file-which' 'msgpack-c' 'rocm-cmake' 'llvm-amdgpu'
             'gcc-fortran')
_rocblas='https://github.com/ROCmSoftwarePlatform/rocBLAS'
source=("$pkgname-$pkgver.tar.gz::$_rocblas/archive/rocm-$pkgver.tar.gz")
sha256sums=('78e37a7597b581d90a29e4b956fa65d0f8d1c8fb51667906b5fe2a223338d401')
options=(!strip)
_dirname="$(basename "$_rocblas")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # fix broken build with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  PATH="/opt/rocm/llvm/bin:${PATH}" \
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_PREFIX_PATH=/opt/rocm/llvm/lib/cmake/llvm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_WITH_TENSILE=ON \
        -DBUILD_WITH_TENSILE_HOST=ON \
        -DTensile_LIBRARY_FORMAT=yaml \
        -DTensile_COMPILER=hipcc \
        -DTensile_ARCHITECTURE=all \
        -DTensile_LOGIC=asm_full \
        -DTensile_CODE_OBJECT_VERSION=V3 \
        -DBUILD_CLIENTS_TESTS=OFF \
        -DBUILD_CLIENTS_BENCHMARKS=OFF \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_TESTING=OFF

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
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
