# Maintainer: Christopher Arndt <aur -at- chrisarndt -dot- de>

_projname='pigpio'
pkgname="python-${_projname}"
pkgver=67
pkgrel=3
pkgdesc="A C and Python library for controlling GPIOs on a Raspberry Pi"
url="http://abyz.co.uk/rpi/pigpio/"
license=('custom:UNLICENSE')
arch=('i686' 'x86_64' 'aarch64')
depends=('python')
source=("${_projname}-${pkgver}.tar.gz::https://github.com/joan2937/pigpio/archive/V${pkgver}.tar.gz")
sha256sums=('4255310dd11ed81035b60711becad081a1eaad2905f704e3eb84e692ca7e4c3d')


prepare() {
  cd "${_projname}-${pkgver}"
  sed -e '/ldconfig/d' -i Makefile
  sed -e '/which python2/d' -i Makefile
  sed -e '/\/opt/d' -i Makefile
  sed -e 's|\$(prefix)/man|\$(prefix)/share/man|' -i Makefile
  sed -e 's|setup.py install|setup.py install --root="'"${pkgdir}"'/"|g' -i Makefile
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
