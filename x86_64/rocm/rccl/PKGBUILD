# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contriubtor: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rccl
pkgver=5.3.0
pkgrel=1
pkgdesc="ROCm Communication Collectives Library"
arch=('x86_64')
url='https://rccl.readthedocs.io/en/rocm-5.3.0/'
license=('custom')
depends=('hip' 'rocm-smi-lib')
makedepends=('cmake' 'python' 'gtest')
_git='https://github.com/ROCmSoftwarePlatform/rccl'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('51da5099fa58c2be882319cebe9ceabe2062feebcc0c5849e8c109030882c10a')
_dirname="$(basename $_git)-$(basename ${source[0]} .tar.gz)"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_CXX_COMPILER=/opt/rocm/hip/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DBUILD_TESTS=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

  install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
