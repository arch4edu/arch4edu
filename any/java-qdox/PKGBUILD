# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>

pkgname=java-qdox
pkgver=2.0.1
pkgrel=1
pkgdesc='A high speed, small footprint parser for extracting class/interface/method definitions from source files complete with JavaDoc @tags'
arch=('any')
url="https://github.com/paul-hammant/qdox"
license=('APACHE')
depends=('java-runtime')
source=("https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/${pkgver}/qdox-${pkgver}.jar"{,.asc})
sha512sums=('def3f6343eba6efe5545c7c94b9a0e650caa0045ec90b3d649dc0050f1a27a0fa8f9f9615ccd1e9a6ede216bdf608e2ca0492d701c27f57c38813942f0123f69'
            'SKIP')
noextract=("qdox-${pkgver}.jar")
validpgpkeys=('B02137D875D833D9B23392ECAE5A7FB608A0221C') # Robert Scholte <rfscholte@apache.org>

package() {
  install -Dm644 "${srcdir}/qdox-${pkgver}.jar" "${pkgdir}/usr/share/java/qdox/qdox.jar"
}
