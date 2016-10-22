# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname='jlatexmath-fop'
pkgver='1.0.3'
pkgrel='1'
pkgdesc='JLaTeXMath FOP plugin'
arch=('any')
url='http://forge.scilab.org/index.php/p/jlatexmath/'
license=('APACHE')
depends=('java-runtime' 'jlatexmath')
source=("http://forge.scilab.org/index.php/p/jlatexmath/downloads/get/${pkgname}-${pkgver}.jar")
noextract=("${pkgname}-${pkgver}.jar")
md5sums=('ecfb78572642dcbf344ed3a25fa1e7c4')

package() {
	install -Dm644 "${srcdir}/${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/jlatexmath/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
