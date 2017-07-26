# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-${_pkgname}
pkgver=6.12
pkgrel=1
pkgdesc='A testing framework inspired from JUnit and NUnit'
arch=('any')
url='http://testng.org/doc/index.html'
license=('APACHE')
depends=("java-runtime")
source=("https://dl.bintray.com/cbeust/maven/org/${_pkgname}/${_pkgname}/${pkgver}/${_pkgname}-${pkgver}.jar")
sha256sums=('9f9f64cb42cbb0771600c7796a527d13a8cf9f7818fd9fb0f9923d73307e5a8d')

package() {
  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}.jar" \
    "${pkgdir}/usr/share/java/${_pkgname}/${_pkgname}-${pkgver}.jar"
}
