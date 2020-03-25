# Maintainer: Jakub Okoński <jakub@okonski.org>
# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=rocminfo
pkgver=3.1.0
pkgrel=1
pkgdesc="ROCm info tools - rocm_agent_enumerator"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/rocminfo"
license=('custom:NCSAOSL')
depends=('pciutils' 'rocm-cmake' 'rocr-runtime' 'roct-thunk-interface')
makedepends=('cmake')
source=("https://github.com/RadeonOpenCompute/rocminfo/archive/roc-$pkgver.tar.gz")
sha256sums=('f024fef05e5ea5bc7316d4bddb5562cbac7048183c351cdb8afd4156ff4c049c')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_PREFIX_PATH=/opt/rocm \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DROCM_DIR=/opt/rocm \
        "$srcdir/$pkgname-roc-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
}
