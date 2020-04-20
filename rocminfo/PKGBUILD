# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=rocminfo
pkgver=3.3.0
pkgrel=4
pkgdesc='ROCm info tools - rocm_agent_enumerator'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocminfo'
license=('custom:NCSAOSL')
depends=('pciutils' 'python' 'hsa-rocr' 'hsa-ext-rocr')
makedepends=('cmake' 'rocm-cmake')
source=("$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('e666f662c9e465aaabbbd0b109d87e017243cdf1a0898fabf5a90947bb3dbcd7')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_PREFIX_PATH=/opt/rocm \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DROCM_DIR=/opt/rocm \
        "$_dirname"
  make
}

package() {
  DESTDIR="$pkgdir" make install
  mkdir -p "$pkgdir/usr/bin"
  ln -st "$pkgdir/usr/bin" /opt/rocm/bin/rocminfo
}
