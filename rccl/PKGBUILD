# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rccl
pkgver=3.8.0
pkgrel=1
pkgdesc="ROCm Communication Collectives Library"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rccl"
license=('custom')
depends=('hip')
makedepends=('cmake' 'python' 'rocminfo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('0b6676d06bdb1f65d511a95db9f842a3443def83d75759dfdf812b5e62d8c910')
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
