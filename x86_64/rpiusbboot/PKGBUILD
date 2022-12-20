#
# Maintainer: Uffe Jakobsen <uffe@uffe.org>
#

pkgname=rpiusbboot
_pkgname=usbboot
_pkgver=20221215-105525
pkgver=${_pkgver//-/_}
pkgrel=1
pkgdesc="Raspberry Pi USB boot"
arch=("i686" "x86_64")
url="https://github.com/raspberrypi/usbboot"
license=("Apache")
depends=("libusb")
conflict=()

source=("https://github.com/raspberrypi/${_pkgname}/archive/refs/tags/${_pkgver}.tar.gz")
sha256sums=('2f02dbe9a88e9dfad5f05e513e1f30afd47b1575820f7c3b09665dfefc45bbaa')

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
  #install -d ${pkgdir}/usr/lib/udev/rules.d/
  #install -D -m 644 debian/70-rpiboot.rules ${pkgdir}/usr/lib/udev/rules.d/
}

#
# EOF
#
