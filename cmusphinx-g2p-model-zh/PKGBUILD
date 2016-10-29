# Maintainer: Jan Holthuis <holthuis.jan@googlemail.com>

pkgname=cmusphinx-g2p-model-zh
_lang=zh
pkgver=0.20120820
pkgrel=1
pkgdesc="CMU Sphinx G2P model for Chinese"
arch=('any')
url="http://sourceforge.net/projects/cmusphinx/files/G2P%20Models/"
license=('custom')
optdepends=('openfst: fst model parsing'
            'phonetisaurus: command line g2p conversion')
source=("http://sourceforge.net/projects/cmusphinx/files/G2P%20Models/${_lang}.tar.gz")
sha256sums=('d77d469a7d6444dec8d0ddfc07fe92ba34109e626a462196b55d7a3ffadf692f')

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