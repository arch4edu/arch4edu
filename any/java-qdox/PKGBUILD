# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>

pkgname=java-qdox
pkgver=2.0.3
pkgrel=1
pkgdesc='A high speed, small footprint parser for fully extracting class/interface/method definitions (including annotations, parameters, param names)'
arch=('any')
url="https://github.com/paul-hammant/qdox"
license=('APACHE')
depends=('java-runtime')
source=("https://repo1.maven.org/maven2/com/thoughtworks/qdox/qdox/${pkgver}/qdox-${pkgver}.jar"{,.asc})
sha512sums=('f1844c1a1752c6ab7bea4832736f2c9461bc1d36e2e65138f2893e480570f1fc84cb85a5f729cf58f3a63a2d81a753df7007f71ebe2ba456a48cdc51d8579ccb'
            'SKIP')
noextract=("qdox-${pkgver}.jar")
validpgpkeys=('B02137D875D833D9B23392ECAE5A7FB608A0221C') # Robert Scholte <rfscholte@apache.org>

package() {
  install -Dm644 "${srcdir}/qdox-${pkgver}.jar" "${pkgdir}/usr/share/java/qdox/qdox.jar"
}
