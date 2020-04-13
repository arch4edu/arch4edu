# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsakmt-roct
pkgver=3.3.0
pkgrel=1
pkgdesc="Radeon Open Compute Thunk Interface"
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface'
license=('MIT')
depends=('numactl' 'pciutils')
makedepends=('cmake')
provides=("roct-thunk-interface=$pkgver")
replaces=('roct-thunk-interface')
source=("$url/archive/roc-$pkgver.tar.gz")
sha256sums=('2cabe9d2cfa72031c05d11290837c476182e72d8dec2049298f691143fdd212b')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm "$_dirname"
  make all build-dev
}

package() {
  make DESTDIR="$pkgdir" install install-dev

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
    /opt/rocm/lib
EOF
}
