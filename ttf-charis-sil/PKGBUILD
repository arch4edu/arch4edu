# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-charis-sil
pkgver=6.101
pkgrel=1
pkgdesc='Font family supporting Latin and Cyrillic scripts. Designed for legibility and publishing.'
arch=('any')
url='https://software.sil.org/charis/'
license=('OFL')
source=("https://software.sil.org/downloads/r/charis/CharisSIL-${pkgver}.zip")
sha256sums=('2de585f4517636d18039f1dc082258dfb89262d7a7feea2526fb21c0cc69131f')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ${srcdir}/CharisSIL-${pkgver}/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${srcdir}/CharisSIL-${pkgver}/OFL.txt ${pkgdir}/usr/share/licenses/${pkgname}/OFL.txt
}
