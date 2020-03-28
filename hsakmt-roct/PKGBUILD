# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsakmt-roct
pkgver=3.1.0
pkgrel=1
pkgdesc="Radeon Open Compute Thunk Interface"
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface'
license=('MIT')
depends=('numactl' 'pciutils')
makedepends=('cmake')
provides=("roct-thunk-interface=$pkgver")
replaces=('roct-thunk-interface')
source=("$pkgname.tar.gz::$url/archive/roc-$pkgver.tar.gz")
sha256sums=('b08176b5f4af39d0160990f9f1dea5d27974f9282f544140b4a41d19446fe570')

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm "ROCT-Thunk-Interface-roc-$pkgver"
  make all build-dev
}

package() {
  make DESTDIR="$pkgdir" install install-dev

  install -Dm644 "ROCT-Thunk-Interface-roc-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
/opt/rocm/lib
EOF
}
