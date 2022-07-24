# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naether.markus@gmail.com>
pkgname=hipblas
pkgver=5.2.1
pkgrel=1
pkgdesc='ROCm BLAS marshalling library'
arch=('x86_64')
url='https://hipblas.readthedocs.io/en/latest/'
license=('MIT')
depends=('hip' 'rocblas' 'rocsolver')
makedepends=('cmake' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/hipBLAS'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "include-path.patch::https://github.com/ROCmSoftwarePlatform/hipBLAS/commit/84b593c7c6acf176b21841a0441801d5a254c62b.patch")
sha256sums=('ccae36b118b7a1eb4b2f7d65fb163f54ab9c5cf774dbe2ec60971d4f78ae8308'
            '34652acc94caad9cf9b22fcf7658b7c7a3fb4c1b517b3aa15e5cc35e973b4fc6')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    # See https://github.com/ROCmSoftwarePlatform/hipBLAS/commit/84b593c7c6acf176b21841a0441801d5a254c62b
    cd "$_dirname"
    patch -Np1 -i "$srcdir/include-path.patch"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipblas.conf" <<EOF
/opt/rocm/hipblas/lib
EOF
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
