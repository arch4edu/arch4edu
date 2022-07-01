# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=5.2.0
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocsparse.readthedocs.io/en/master/'
license=('MIT')
depends=('hip' 'rocprim')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('7ed929af16d2502135024a6463997d9a95f03899b8a33aa95db7029575c89572')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

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
