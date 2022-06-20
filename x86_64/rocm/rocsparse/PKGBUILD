# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=5.1.3
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocsparse'
license=('MIT')
depends=('hip' 'rocprim')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('ef9641045b36c9aacc87e4fe7717b41b1e29d97e21432678dce7aca633a8edc2')
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
  # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-5.1.x/docs/markdown/clang_options.md
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
