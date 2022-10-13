# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
pkgver=5.3.0
pkgrel=1
pkgdesc='Next generation BLAS implementation for ROCm platform'
arch=('x86_64')
url='https://rocblas.readthedocs.io/en/latest'
license=('MIT')
depends=('hip' 'openmp')
makedepends=('rocm-cmake' 'git' 'python' 'python-pip' 'python-virtualenv' 'python-pyaml'
             'perl-file-which' 'msgpack-c' 'gcc-fortran')
_rocblas='https://github.com/ROCmSoftwarePlatform/rocBLAS'
source=("$pkgname-$pkgver.tar.gz::$_rocblas/archive/rocm-$pkgver.tar.gz")
sha256sums=('8ea7269604cba949a6ea84b78dc92a44fa890427db88334da6358813f6512e34')
options=(!lto)
_dirname="$(basename "$_rocblas")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Appendix_A.html
  PATH="/opt/rocm/llvm/bin:${PATH}" \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_PREFIX_PATH=/opt/rocm/llvm/lib/cmake/llvm \
    -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
    -DBUILD_WITH_TENSILE=ON \
    -DTensile_LIBRARY_FORMAT=yaml \
    -DTensile_CODE_OBJECT_VERSION=V3 \
    -DCMAKE_TOOLCHAIN_FILE=toolchain-linux.cmake \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/rocblas.conf"

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
