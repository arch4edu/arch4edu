# Maintainer: Jan Holthuis <holthuis.jan@googlemail.com>

pkgname=cmusphinx-g2p-model-es
_lang=es
pkgver=0.20120820
pkgrel=1
pkgdesc="CMU Sphinx G2P model for Spanish"
arch=('any')
url="http://sourceforge.net/projects/cmusphinx/files/G2P%20Models/"
license=('custom')
optdepends=('openfst: fst model parsing'
            'phonetisaurus: command line g2p conversion')
source=("http://sourceforge.net/projects/cmusphinx/files/G2P%20Models/${_lang}.tar.gz")
sha256sums=('62a762e41545099018044ecae5c47d93ff4b201d2e0b01634e0088cb17678cd7')

prepare() {
    cd "${srcdir}"
	mv "${_lang}/LICENSE" "LICENSE"
	mv "${_lang}/README" "README"
}

package() {
    cd "${srcdir}"
    install -D -m 644 "README" "${pkgdir}/usr/share/doc/${pkgname}/README"
    install -D -m 644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -d -m 755 "${pkgdir}/usr/share/cmusphinx/g2p_models"
  	cp -dr --preserve=mode,timestamp "${_lang}" "${pkgdir}/usr/share/cmusphinx/g2p_models"
 }