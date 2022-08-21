# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=hipsparse
pkgver=5.2.3
pkgrel=1
pkgdesc='rocSPARSE marshalling library.'
arch=('x86_64')
url='https://hipsparse.readthedocs.io/en/latest/'
license=('MIT')
depends=('hip' 'rocsparse')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/hipSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('f70d3deff13188adc4105ef3ead53510e4b54075b9ffcfe3d3355d90d4b6eadd')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  HIP_PATH=/opt/rocm \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipsparse.conf" << EOF
/opt/rocm/hipsparse/lib
EOF
  install -Dm644 "$srcdir/hipSPARSE-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
