# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Hussam Al-Tayeb <ht990332@gmail.com>
pkgname=xalan-java
pkgver=2.7.3
pkgrel=1
pkgdesc="XSLT processor for transforming XML documents into HTML, text, or other XML document types"
arch=(any)
license=(Apache-2.0)
url="https://xalan.apache.org"
depends=('java-runtime-headless')
source=(https://dlcdn.apache.org/xalan/xalan-j/binaries/xalan-j_${pkgver//./_}-bin.tar.gz{,.asc})
sha512sums=('18373698936776e9ce5818e9ffbf4efe56c44d52ca094b85fa438a59528c369acb27d07afbc85295bbc44698876887616f65d7bc6364defa08b36561e8b3ddc7'
  'SKIP')
validpgpkeys=('4D8FB572FB6ADCFD69CBFE0D7B2586A6B5E25C3D') # Mukul Gandhi (CODE SIGNING KEY) <mukulg@apache.org>

package() {
  cd xalan-j_${pkgver//./_}
  install -m755 -d "${pkgdir}"/usr/share/java
  install -m644 serializer.jar "${pkgdir}"/usr/share/java
  install -m644 xalan.jar "${pkgdir}"/usr/share/java
  install -m644 xercesImpl.jar "${pkgdir}"/usr/share/java
  install -m644 xml-apis.jar "${pkgdir}"/usr/share/java
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
