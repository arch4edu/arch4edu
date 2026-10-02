#
# Maintainer: Uffe Jakobsen <uffe@uffe.org>
#

pkgname=rpiusbboot
_pkgname=usbboot
_pkgver=20261002-115811
pkgver=${_pkgver//-/_}
pkgrel=1
pkgdesc="Raspberry Pi USB boot"
arch=("i686" "x86_64")
url="https://github.com/raspberrypi/usbboot"
license=("Apache-2.0")
depends=("glibc" "libusb")
conflict=()

source=("https://github.com/raspberrypi/${_pkgname}/archive/refs/tags/${_pkgver}.tar.gz")
sha256sums=("9312b27a85da28bf7b356f3955389f13314c3bba73f0f6bee2df95517d3d3a46")

#pkgver()
#{
#  cd "${srcdir}/${_pkgname}"
#  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
#}

build()
{
  cd "${srcdir}/${_pkgname}-${_pkgver}"
  make || return 1
}

package()
{
  cd "${srcdir}/${_pkgname}-${_pkgver}"
  #make DESTDIR="${pkgdir}/" install
  install -D rpiboot ${pkgdir}/usr/bin/rpiusbboot
  install -d ${pkgdir}/etc/udev/rules.d/
  install -D -m 644 debian/70-rpiboot.rules ${pkgdir}/etc/udev/rules.d/
}

#
# EOF
#
