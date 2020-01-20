# Maintainer: Pedro Gabriel <pedrogabriel@dcc.ufmg.br>
# Maintainer: FadeMind <fademind@gmail.com>

_fwname=aic94xx
pkgname=${_fwname}-firmware
pkgver=30
pkgrel=9
pkgdesc="Adaptec SAS 44300, 48300, 58300 Sequencer Firmware for AIC94xx driver"
url="https://storage.microsemi.com/en-us/speed/scsi/linux/${_fwname}-seq-${pkgver}-1_tar_gz.php"
license=('custom')
arch=('any')
source=("${_fwname}-seq-${pkgver}-1.tar.gz::http://download.adaptec.com/scsi/linux/${_fwname}-seq-${pkgver}-1.tar.gz"
        "LICENSE.${_fwname}")
sha256sums=('0608a919b95e65e8fe3c0cbc15f7e559716bda39a6efca863417a65f75e15478'
            '6e0dd2831a66437e87659ed31384f11bdc7720bc539d2efa063fbb7f4ac0e46c')

build() {
    bsdtar xvf "${_fwname}_seq-${pkgver}-1.noarch.rpm"
    chmod 644  "${srcdir}/lib/firmware/${_fwname}-seq.fw"
}

package() {
    install -Dm644 ${srcdir}/lib/firmware/${_fwname}-seq.fw ${pkgdir}/usr/lib/firmware/${_fwname}-seq.fw
    install -Dm644 ${srcdir}/LICENSE.${_fwname}             ${pkgdir}/usr/share/doc/${pkgname}/LICENSE.${_fwname}
    install -Dm644 ${srcdir}/README-94xx.pdf                ${pkgdir}/usr/share/doc/${pkgname}/README-94xx.pdf
}
