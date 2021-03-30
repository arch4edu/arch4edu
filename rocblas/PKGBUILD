# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
pkgver=4.1.0
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
sha256sums=('8be20c722bab169bc4badd79a9eab9a1aa338e0e5ff58ad85ba6bf09e8ac60f4')
options=(!strip)
_dirname="$(basename "$_rocblas")-$(basename "${source[0]}" ".tar.gz")"

build() {

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

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocblas.conf" << EOF
/opt/rocm/rocblas/lib
EOF
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
