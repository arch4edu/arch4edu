# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>

pkgname='jlatexmath'
pkgver='1.0.3'
pkgrel='1'
pkgdesc='Java API to display mathematical formulas written in LaTeX'
arch=('any')
url='http://forge.scilab.org/index.php/p/jlatexmath/'
license=('APACHE')
depends=('java-runtime')
source=(
"http://forge.scilab.org/index.php/p/jlatexmath/downloads/get/${pkgname}-${pkgver}.jar"
)
noextract=("${pkgname}-${pkgver}.jar")
md5sums=('502cd06e4c07e95deeb95add1abc1487')

package() {
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
