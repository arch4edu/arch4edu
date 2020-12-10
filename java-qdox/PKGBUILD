# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>

pkgname=java-qdox
pkgver=2.0.0
pkgrel=1
pkgdesc='A high speed, small footprint parser for extracting class/interface/method definitions from source files complete with JavaDoc @tags'
arch=('any')
url="https://github.com/paul-hammant/qdox"
license=('APACHE')
depends=('java-runtime')
source=("https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/${pkgver}/qdox-${pkgver}.jar"{,.asc})
md5sums=('99c6b1d92cd9c3b60676f9f4391c17b0'
         'SKIP')
sha1sums=('a31dacde4a80ff171a8e6a7e3d5913a51ee22f06'
          'SKIP')
sha256sums=('dcb91eed164a37b11d28bf6c8adfc627f294561e978c92f805820a86b290dd48'
            'SKIP')
noextract=("qdox-${pkgver}.jar")
validpgpkeys=('B02137D875D833D9B23392ECAE5A7FB608A0221C') # Robert Scholte <rfscholte@apache.org>

package() {
  install -Dm644 "${srcdir}/qdox-${pkgver}.jar" "${pkgdir}/usr/share/java/qdox/qdox.jar"
}
