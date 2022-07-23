# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=5.2.1
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocsparse.readthedocs.io/en/master/'
license=('MIT')
depends=('hip' 'rocprim')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "gfx1010.patch::$_git/commit/f8934f91f779c291a5cf1157ed58fc427544fd2d.patch")
sha256sums=('01f3535442740221edad2cde0a20b2499c807f6733d5016b33c47f34a5a55c49'
            '97e250d386ba318550701bc0f0657d5f7ba282f301c7d81b1bbb1563af9dbe56')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/gfx1010.patch"
}

build() {
  local cmake_flags=(
        '-DCMAKE_INSTALL_PREFIX=/opt/rocm'
        '-Drocprim_DIR=/opt/rocm/rocprim/rocprim/lib/cmake/rocprim'
        '-DBUILD_CLIENTS_SAMPLES=OFF')
  if [[ -n "$AMDGPU_TARGETS" ]]; then
      cmake_flags+=("-DAMDGPU_TARGETS=$AMDGPU_TARGETS")
  fi

  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        "${cmake_flags[@]}"
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocsparse.conf" <<EOF
/opt/rocm/rocsparse/lib
EOF
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
