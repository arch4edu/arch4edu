# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>

pkgname=fop-hyph
pkgver=2.1
pkgrel=1
pkgdesc="The hyphenation pattern files compiled for FOP"
arch=('any')
url="http://offo.sourceforge.net/"
license=('unknown')
depends=('java-runtime' 'fop>=1.0')
source=("http://sourceforge.net/projects/offo/files/offo-hyphenation/${pkgver}/offo-hyphenation-binary.zip")
md5sums=('0a93418cc53c999dfcfbf7ec891fd7d9')

package() {
	cd "${srcdir}/offo-hyphenation-binary/"
	install -Dm644 "${pkgname}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
