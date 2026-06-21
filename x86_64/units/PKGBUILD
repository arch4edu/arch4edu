# Maintainer: tarball <bootctl@gmail.com>
# Contributor: ModelHX
# Contributor: Kyle Keen <keenerd@gmail.com>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Jeff Mickey <jeff@archlinux.org>
# Contributor: Steve Sansom <snsansom@gmail.com>
# Contributor: qubidt <qubidt at gmail dot com>

pkgname=units
pkgver=2.27
pkgrel=1
pkgdesc="converts between different units"
arch=('x86_64' 'aarch64' 'armv7h' 'riscv64')
url="https://www.gnu.org/software/units/units.html"
depends=('readline')
# NOTE: set the PAGER env var to use own pager
optdepends=('less: default pager for built-in documentation'
            'python-requests: for live currency rates')
makedepends=('python-requests')
license=("GPL-3.0-or-later")
options=('!makeflags')
validpgpkeys=(
  '927D02FA733C3D902D21CAC02D649F2B7B4C8179' # Adrian Mariano <avm4@cornell.edu>
)
source=(https://ftp.gnu.org/gnu/units/$pkgname-$pkgver.tar.gz{,.sig}
        'units_currency.timer'
        'units_currency.service'
        '0000-pager.patch')
sha256sums=('e1bbdb09672e7c08eee986749e7a1629eb84a6bdf41f5a2a79d6804444abbe10'
            'SKIP'
            'c1cb48a6157c850a0b7ecbf4387b82820d6e42f4a2c7ff0eb9de293bad6b128f'
            '52e8cd68110e797e3ee3737f06200505225039b18f3f9b87ae38b6c539c9ccb2'
            'fb31ebf4735fdd443df72733b6f1cc08da8e4dbee422636d0d3486db6cff6eb1')

prepare() {
  cd "$pkgname-$pkgver"
  patch -p1 <"$srcdir/0000-pager.patch"
}

build() {
  cd "$pkgname-$pkgver"
  ./configure --prefix=/usr --datadir=/usr/share --sharedstatedir=/var/lib
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  rm "$pkgdir/usr/share/units/currency.units"
  ln -s /var/lib/units/currency.units "$pkgdir/usr/share/units/currency.units"
  install -Dm644 ../units_currency.timer "$pkgdir/usr/lib/systemd/system/units_currency.timer"
  install -Dm644 ../units_currency.service "$pkgdir/usr/lib/systemd/system/units_currency.service"
}
