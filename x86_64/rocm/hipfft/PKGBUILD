# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=hipfft
pkgver=5.2.3
pkgrel=1
pkgdesc='rocFFT marshalling library.'
arch=('x86_64')
url='https://hipfft.readthedocs.io/en/latest/'
license=('MIT')
depends=('hip' 'rocfft')
makedepends=('cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/hipFFT'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('10be731fe91ede5e9f254f6eb3bc00b4dbeab449477f3cac03de358a7d0a6fa1')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  local cmake_args=(-DCMAKE_INSTALL_PREFIX=/opt/rocm
                    -DBUILD_CLIENTS_SAMPLES=OFF
                    -DBUILD_CLIENTS_TESTS=OFF)
  if [[ -n "$AMDGPU_TARGETS" ]]; then
      cmake_args+=(-DAMDGPU_TARGETS="$AMDGPU_TARGETS")
  fi
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        "${cmake_args[@]}"
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipfft.conf" << EOF
/opt/rocm/hipfft/lib
EOF
  install -Dm644 "$srcdir/$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
