# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: Markus Näther <naether.markus@gmail.com>
pkgname=rocblas
pkgver=5.4.1
pkgrel=1
pkgdesc='Next generation BLAS implementation for ROCm platform'
arch=('x86_64')
url='https://rocblas.readthedocs.io/en/latest'
license=('MIT')
depends=('hip' 'openmp')
makedepends=('rocm-cmake' 'python' 'python-virtualenv' 'python-pyaml' 'python-wheel'
             'perl-file-which' 'python-msgpack' 'msgpack-cxx' 'gcc-fortran')
_rocblas='https://github.com/ROCmSoftwarePlatform/rocBLAS'
_tensile='https://github.com/ROCmSoftwarePlatform/Tensile'
source=("$pkgname-$pkgver.tar.gz::$_rocblas/archive/rocm-$pkgver.tar.gz"
        "$pkgname-tensile-$pkgver.tar.gz::$_tensile/archive/refs/tags/rocm-$pkgver.tar.gz")
sha256sums=('2f6d30b025306ba5f378154eb0494ac9260190120d085b67c3f499e7d2b6a70b'
            '6bcc08426c14c203c799c93815293c2a17d5b656936536dcece1302d53816cef')
options=(!lto)
_dirname="$(basename "$_rocblas")-$(basename "${source[0]}" ".tar.gz")"
_tensile_dir="$(basename "$_tensile")-$(basename "${source[1]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html
  PATH="/opt/rocm/llvm/bin:/opt/rocm/bin:${PATH}" \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_PREFIX_PATH=/opt/rocm/llvm/lib/cmake/llvm \
    -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
    -DBUILD_WITH_TENSILE=ON \
    -DTensile_LIBRARY_FORMAT=yaml \
    -DTensile_CODE_OBJECT_VERSION=V3 \
    -DCMAKE_TOOLCHAIN_FILE=toolchain-linux.cmake \
    -DTensile_TEST_LOCAL_PATH="$srcdir/$_tensile_dir"
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/rocblas.conf"

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
