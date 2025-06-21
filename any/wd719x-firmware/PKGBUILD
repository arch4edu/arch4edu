# Maintainer: Mijail Rondon Viloria <mijailr>
# Contributor: Fademind
# Contributor: pedrogabriel

pkgname=wd719x-firmware
pkgver=1
pkgrel=9
pkgdesc="Firmware for Western Digital WD7193, WD7197, and WD7296 SCSI cards"
arch=('any')
url="https://github.com/mijailr/wd719x-firmware"
license=('custom')
makedepends=('lhasa')
source=("https://github.com/mijailr/wd719x-firmware/raw/master/pciscsi.exe")
sha256sums=('d310338eaaeae6db3673021c0ec2ec23b9cfb9f9b9d1eb8854d2d60b3a6490f9')
noextract=('pciscsi.exe')

build() {
  cd "${srcdir}"

  lha xi pciscsi.exe pci-scsi.exe
  lha xi pci-scsi.exe nt/wd7296a.sys

  dd if=wd7296a.sys of=wd719x-risc.bin bs=1 skip=5760 count=14336 status=none
  dd if=wd7296a.sys of=wd719x-wcs.bin bs=1 skip=20096 count=514 status=none
}

package() {
  install -m644 -Dt "${pkgdir}/usr/lib/firmware" wd719x-risc.bin wd719x-wcs.bin
}
