# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Maintainer: Guillaume ALAUX <guillaume@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=xerces2-java
pkgver=2.12.1
pkgrel=1
pkgdesc="High performance fully compliant Java XML parser"
arch=('any')
url="https://xml.apache.org/xerces2-j"
license=('APACHE')
depends=('java-runtime' 'java-resolver')
provides=("java-xerces2=${pkgver}")
conflicts=('java-xerces2')
replaces=('java-xerces2')
source=(https://downloads.apache.org/xerces/j/binaries/Xerces-J-bin.$pkgver.tar.gz{,.asc})
sha512sums=('896e2474b2e2e5076778e8112c8d18753a8214396975491382ecec1e4fd7e6dab3c2cab1d511d83903ad2858e6d15bdd1e26371d04ffbc1bb09248b60e5c13a9'
            'SKIP')
validpgpkeys=('4D8FB572FB6ADCFD69CBFE0D7B2586A6B5E25C3D') # Mukul Gandhi (CODE SIGNING KEY) <mukulg@apache.org>

package() {
  cd xerces-${pkgver//./_}
  install -dm755 "${pkgdir}"/usr/share/java
  install -m644 {serializer,xercesImpl,xml-apis}.jar "${pkgdir}"/usr/share/java/
}
