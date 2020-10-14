# Maintainer: Christopher Arndt <aur -at- chrisarndt -dot- de>

_projname='pigpio'
pkgname="python-${_projname}"
pkgver=78
pkgrel=1
pkgdesc="A C and Python library for controlling GPIOs on a Raspberry Pi"
url="http://abyz.me.uk/rpi/pigpio/"
license=('custom:UNLICENSE')
arch=('i686' 'x86_64' 'aarch64' 'armv7h')
depends=('python')
source=("${_projname}-${pkgver}.tar.gz::https://github.com/joan2937/pigpio/archive/v${pkgver}.tar.gz")
sha256sums=('ef4a4dc7ca8ca2f97fbdb9fd75586f61be7222d0f6c14e58af6c9192ad42f682')


prepare() {
  cd "${_projname}-${pkgver}"
  sed -e '/which python2/d' -i Makefile
  sed -e '/\/opt/d' -i Makefile
  sed -e 's|\$(prefix)/man|\$(prefix)/share/man|' -i Makefile
  sed -e 's|/usr/bin/pigpiod|/usr/bin/pigpiod -g|' -i util/pigpiod.service
}

build() {
  cd "${_projname}-${pkgver}"
  make
}

package() {
  cd "${_projname}-${pkgver}"
  make prefix=/usr DESTDIR="${pkgdir}" install
  install -Dm644 util/pigpiod.service -t "${pkgdir}/usr/lib/systemd/system"
  install -Dm644 UNLICENCE -t "${pkgdir}/usr/share/licenses/$pkgname"
}
