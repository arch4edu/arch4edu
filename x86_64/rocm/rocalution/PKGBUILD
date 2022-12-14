# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocalution
pkgver=5.4.0
pkgrel=1
pkgdesc='Next generation library for iterative sparse solvers for ROCm platform'
arch=('x86_64')
url='https://rocalution.readthedocs.io/en/master'
license=('MIT')
depends=('hip' 'rocsparse' 'rocblas' 'rocprim' 'rocrand' 'openmp')
makedepends=('rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocALUTION'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "$pkgname-remove-git.patch::$_git/commit/773e8be7354bbc961d86810dbb23e6248f6e513b.patch")
sha256sums=('dccf004434e0fee6d0c7bedd46827f5a2af0392bc4807a08403b130e461f55eb'
            '9daafee87896ef043b655542f36e078b9a3f3a4a106b69849cfd8add25637cca')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/$pkgname-remove-git.patch"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DROCM_PATH=/opt/rocm \
    -DHIP_ROOT_DIR=/opt/rocm/hip \
    -DSUPPORT_HIP=ON \
    -DSUPPORT_OMP=ON \
    -DSUPPORT_MPI=OFF \
    -DBUILD_SHARED_LIBS=ON
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/rocalution.conf"

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
