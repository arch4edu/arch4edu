# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
pkgver=5.2.1
pkgrel=1
pkgdesc='Next generation BLAS implementation for ROCm platform'
arch=('x86_64')
url='https://rocblas.readthedocs.io/en/latest'
license=('MIT')
depends=('hip' 'openmp')
makedepends=('cmake' 'git' 'python' 'python-pip' 'python-virtualenv' 'python-pyaml'
             'perl-file-which' 'msgpack-c' 'rocm-cmake' 'gcc-fortran')
_rocblas='https://github.com/ROCmSoftwarePlatform/rocBLAS'
source=("$pkgname-$pkgver.tar.gz::$_rocblas/archive/rocm-$pkgver.tar.gz"
        "include-path.patch::https://github.com/ROCmSoftwarePlatform/rocBLAS/commit/992429ff1d04195b10f9a3350668e180b34dbdb5.patch")
sha256sums=('6be804ba8d9e491a85063c220cd0ddbf3d13e3b481eee31041c35a938723f4c6'
            'SKIP')
options=(!lto)
_dirname="$(basename "$_rocblas")-$(basename "${source[0]}" ".tar.gz")"

# Number of threads for tensile build. Uses all threads by default.
_tensile_threads="$(nproc)"

prepare() {
    # See https://github.com/ROCmSoftwarePlatform/rocBLAS/commit/992429ff1d04195b10f9a3350668e180b34dbdb5
    cd "$_dirname"
    patch -Np1 -i "$srcdir/include-path.patch"
}

build() {
  local cmake_args=(-DCMAKE_INSTALL_PREFIX=/opt/rocm
                    -DCMAKE_PREFIX_PATH=/opt/rocm/llvm/lib/cmake/llvm
                    -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr
                    -DBUILD_WITH_TENSILE=ON
                    -DTensile_LIBRARY_FORMAT=yaml
                    -DTensile_CPU_THREADS="$_tensile_threads"
                    -DTensile_CODE_OBJECT_VERSION=V3
                    -DCMAKE_TOOLCHAIN_FILE=toolchain-linux.cmake
                    -DBUILD_TESTING=OFF)
  if [[ -n "$AMDGPU_TARGETS" ]]; then
      cmake_args+=(-DAMDGPU_TARGETS="$AMDGPU_TARGETS")
  fi
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  PATH="/opt/rocm/llvm/bin:${PATH}" \
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        "${cmake_args[@]}"

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocblas.conf" << EOF
/opt/rocm/rocblas/lib
EOF
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
