# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contriubtor: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rccl
pkgver=5.2.0
pkgrel=1
pkgdesc="ROCm Communication Collectives Library"
arch=('x86_64')
url="https://docs.amd.com/bundle/rccl-release-rocm-rel-5.2/page/library.html"
license=('custom')
depends=('hip' 'rocm-smi-lib')
makedepends=('cmake' 'python' 'gtest')
_git='https://github.com/ROCmSoftwarePlatform/rccl'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('6ee3a04da0d16eb53f768a088633a7d8ecc4416a2d0c07f7ba8426ab7892b060')
_dirname="$(basename $_git)-$(basename ${source[0]} .tar.gz)"

build() {
  local cmake_args=(-DCMAKE_INSTALL_PREFIX=/opt/rocm
                    -DBUILD_TESTS=OFF)
  if [[ -n "$AMDGPU_TARGETS" ]]; then
      cmake_args+=(-DAMDGPU_TARGETS="$AMDGPU_TARGETS")
  fi
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html

  CXX=/opt/rocm/hip/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        "${cmake_args[@]}"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rccl.conf" <<EOF
/opt/rocm/rccl/lib
EOF

  install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
