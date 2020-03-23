# Maintainer: Christopher Arndt <aur -at- chrisarndt -dot- de>

_projname='pigpio'
pkgname="python-${_projname}"
pkgver=75
pkgrel=1
pkgdesc="A C and Python library for controlling GPIOs on a Raspberry Pi"
url="http://abyz.me.uk/rpi/pigpio/"
license=('custom:UNLICENSE')
arch=('i686' 'x86_64' 'aarch64' 'armv7h')
depends=('python')
source=("${_projname}-${pkgver}.tar.gz::https://github.com/joan2937/pigpio/archive/v${pkgver}.tar.gz")
sha256sums=('dfec8d06075a9336433d96a8e2f86810f3332d616cf0d6253d98ad78094aa15a')


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
