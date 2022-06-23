#
# Maintainer: Uffe Jakobsen <uffe@uffe.org>
#

pkgname=rpiusbboot
_pkgname=usbboot
pkgver=2021.07.01
_pkgver=v${pkgver}
pkgrel=1
pkgdesc="Raspberry Pi USB boot"
arch=("i686" "x86_64")
url="https://github.com/raspberrypi/usbboot"
license=("Apache")
depends=("libusb")
conflict=()

  source=("https://github.com/raspberrypi/${_pkgname}/archive/refs/tags/${_pkgver}.tar.gz")
sha256sums=('4565314b38e7c7505b7d32a3b51b49f79c7dd5767d45b86d38e5255ae7489a43')

#pkgver()
#{
#  cd "${srcdir}/${_pkgname}"
#  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
#}

build()
{
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make || return 1
}

package()
{
  cd "${srcdir}/${_pkgname}-${pkgver}"
  #make DESTDIR="${pkgdir}/" install
  install -D rpiboot ${pkgdir}/usr/bin/rpiusbboot
  #install -d ${pkgdir}/usr/lib/udev/rules.d/
  #install -D -m 644 debian/70-rpiboot.rules ${pkgdir}/usr/lib/udev/rules.d/
}

#
# EOF
#
