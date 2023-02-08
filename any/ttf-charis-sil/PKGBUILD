# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-charis-sil
pkgver=6.200
pkgrel=1
pkgdesc='Font family supporting Latin and Cyrillic scripts. Designed for legibility and publishing.'
arch=('any')
url='https://software.sil.org/charis/'
license=('OFL')
source=("https://software.sil.org/downloads/r/charis/CharisSIL-${pkgver}.zip")
sha256sums=('4b09aa75760b8aa697b762c34afb995dde0754c8f09256cb912dbfc478c97ade')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ${srcdir}/CharisSIL-${pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${srcdir}/CharisSIL-${pkgver}/OFL.txt ${pkgdir}/usr/share/licenses/${pkgname}/OFL.txt
}
