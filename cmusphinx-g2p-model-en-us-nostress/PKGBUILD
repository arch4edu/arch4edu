# Maintainer: Jan Holthuis <holthuis.jan@googlemail.com>

pkgname=cmusphinx-g2p-model-en-us-nostress
_lang=en_us_nostress
pkgver=0.20140715
pkgrel=2
pkgdesc="CMU Sphinx G2P model for American English (unstressed)"
arch=('any')
url="http://sourceforge.net/projects/cmusphinx/files/G2P%20Models/"
license=('custom')
optdepends=('openfst: fst model parsing'
            'phonetisaurus: command line g2p conversion')
source=("http://sourceforge.net/projects/cmusphinx/files/G2P%20Models/${_lang}.tar.gz")
sha256sums=('7ac349406bb8f05beefa1f328210e0e0d83461683377ccfe09bfc89f3b1d794f')

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