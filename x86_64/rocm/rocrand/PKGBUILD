# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=rocrand
pkgver=5.2.3
pkgrel=1
pkgdesc='Pseudo-random and quasi-random number generator on ROCm'
arch=('x86_64')
url='https://rocsparse.readthedocs.io/en/master/'
license=('MIT')
depends=('hip')
makedepends=('cmake' 'git' 'gcc-fortran' 'python')
optdepends=('gcc-fortran: Use Fortran wrapper'
            'python: Use Python wrapper')
_git='https://github.com/ROCmSoftwarePlatform/rocRAND'
_hiprand='https://github.com/ROCmSoftwarePlatform/hipRAND'
_commit=20ac3db9d7462c15a3e96a6f0507cd5f2ee089c4
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hiprand-$pkgver.tar.gz::$_hiprand/archive/$_commit.tar.gz")
sha256sums=('01eda8022fab7bafb2c457fe26a9e9c99950ed1b772ae7bf8710b23a90b56e32'
            'ee38a68c9e88056b7ecd41553e496e455dbb3fe08871ff3545430d6733070e6b')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"
_hipname="$(basename "$_hiprand")-$(basename "${source[1]}" ".tar.gz")"

prepare() {
  rm -r "$srcdir/$_dirname/hipRAND"
  ln -sf "$srcdir/$_hipname" "$srcdir/$_dirname/hipRAND"
}

build() {
  local cmake_args=('-DCMAKE_INSTALL_PREFIX=/opt/rocm'
                    '-DBUILD_TEST=OFF')
  if [[ -n "$AMDGPU_TARGETS" ]]; then
    cmake_args+=("-DAMDGPU_TARGETS=${AMDGPU_TARGETS}")
  fi

  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXX=/opt/rocm/hip/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        "${cmake_args[@]}"
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocrand.conf" << EOF
/opt/rocm/hiprand/lib
/opt/rocm/rocrand/lib
EOF
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Some packages search for {roc,hip}rand includes in /opt/rocm/include/{roc,hip}rand
  install -d "$pkgdir/opt/rocm/include"
  ln -s "/opt/rocm/hiprand/include/" "$pkgdir/opt/rocm/include/hiprand"
  ln -s "/opt/rocm/rocrand/include/" "$pkgdir/opt/rocm/include/rocrand"
}
