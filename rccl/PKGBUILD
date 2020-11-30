# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rccl
pkgver=3.9.0
pkgrel=2
pkgdesc="ROCm Communication Collectives Library"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rccl"
license=('custom')
depends=('hip' 'gtest')
makedepends=('cmake' 'python' 'rocminfo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('ff9d03154d668093309ff814a33788f2cc093b3c627e78e42ae246e6017408b0')
_dirname="$(basename $url)-$(basename ${source[0]} .tar.gz)"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DBUILD_TESTS=OFF

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rccl.conf" <<EOF
/opt/rocm/rccl/lib
EOF

  install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
