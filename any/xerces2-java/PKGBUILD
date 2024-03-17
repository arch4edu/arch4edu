# Maintainer:
# Contributor: Andreas Radke <andyrtr@archlinux.org>
# Contributor: Guillaume ALAUX <guillaume@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

_pkgname="xerces2-java"
pkgname="$_pkgname"
pkgver=2.12.2
pkgrel=2
pkgdesc="High performance fully compliant Java XML parser"
url="https://xml.apache.org/xerces2-j"
license=('Apache-2.0')
arch=('any')

depends=('java-runtime')

provides=(
  "java-resolver=1.2"
  "java-xerces2=${pkgver}"
)
conflicts=(
  "java-resolver"
  "java-xerces2"
)

_pkgsrc="xerces-${pkgver//./_}"
source=(
  "https://dlcdn.apache.org/xerces/j/binaries/Xerces-J-bin.$pkgver.tar.gz"{,.asc}
)
sha256sums=(
  '1ad48949b2c7f0df91668f058d6ec773871adb5527b0b5c73dc2160ab5d162e2'
  'SKIP'
)
validpgpkeys=('4D8FB572FB6ADCFD69CBFE0D7B2586A6B5E25C3D') # Mukul Gandhi (CODE SIGNING KEY) <mukulg@apache.org>

package() {
  cd "$_pkgsrc"
  install -Dm644 {resolver,serializer,xercesImpl,xml-apis}.jar -t "$pkgdir/usr/share/java/"
}
