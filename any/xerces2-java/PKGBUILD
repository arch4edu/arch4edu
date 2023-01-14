# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Maintainer: Guillaume ALAUX <guillaume@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=xerces2-java
pkgver=2.12.2
pkgrel=1
pkgdesc="High performance fully compliant Java XML parser"
arch=('any')
url="https://xml.apache.org/xerces2-j"
license=('APACHE')
depends=('java-runtime' 'java-resolver')
provides=("java-xerces2=${pkgver}")
conflicts=('java-xerces2')
replaces=('java-xerces2')
source=(https://dlcdn.apache.org/xerces/j/binaries/Xerces-J-bin.$pkgver.tar.gz{,.asc})
sha512sums=('de3a32258a53a044bf6dcf4f63553be588face141e018fd49b41b91013f941208714b7e21cdba419bd69166ef949253fad1ec937cb84b13a815fe66b91154c38'
            'SKIP')
validpgpkeys=('4D8FB572FB6ADCFD69CBFE0D7B2586A6B5E25C3D') # Mukul Gandhi (CODE SIGNING KEY) <mukulg@apache.org>

package() {
  cd xerces-${pkgver//./_}
  install -dm755 "${pkgdir}"/usr/share/java
  install -m644 {serializer,xercesImpl,xml-apis}.jar "${pkgdir}"/usr/share/java/
}
