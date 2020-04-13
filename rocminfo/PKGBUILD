# Maintainer: Jakub Okoński <jakub@okonski.org>
# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=rocminfo
pkgver=3.3.0
pkgrel=2
pkgdesc="ROCm info tools - rocm_agent_enumerator"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/rocminfo"
license=('custom:NCSAOSL')
depends=('pciutils' 'rocm-cmake' 'hsa-rocr' 'hsa-ext-rocr')
makedepends=('cmake')
source=("https://github.com/RadeonOpenCompute/rocminfo/archive/rocm-$pkgver.tar.gz")
sha256sums=('e666f662c9e465aaabbbd0b109d87e017243cdf1a0898fabf5a90947bb3dbcd7')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_PREFIX_PATH=/opt/rocm \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DROCM_DIR=/opt/rocm \
        "$srcdir/$pkgname-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install
  
  mkdir -p ${pkgdir}/usr/bin
  ln -s ${pkgdir}/opt/rocm/bin/rocminfo ${pkgdir}/usr/bin/rocminfo
}
