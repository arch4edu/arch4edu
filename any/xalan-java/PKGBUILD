
# Contributor: Hussam Al-Tayeb <ht990332@gmail.com>

pkgname=xalan-java
pkgver=2.7.2
pkgrel=3
pkgdesc="XSLT processor for transforming XML documents into HTML, text, or other XML document types"
arch=('any')
license=('APACHE')
url="https://xalan.apache.org/xalan-j/index.html"
depends=('xerces2-java')
source=(https://archive.apache.org/dist/xalan/xalan-j/binaries/xalan-j_${pkgver//./_}-bin-2jars.tar.gz{,.asc})
sha512sums=('6fd7700e2abce4038224a953682b623f46cfa5642bf836de07f2986f8432f1113c23f2d84d478d34b329f0c7e6fd65b9d614efe6ad8bc2e5b46b29fedac4f503'
            'SKIP')
validpgpkeys=('2DB4F1EF0FA761ECC4EA935C86FDC7E2A11262CB') # Gary David Gregory (Code signing key) <ggregory@apache.org>

package() {
  cd xalan-j_${pkgver//./_}
  install -m755 -d "${pkgdir}"/usr/share/java
  install -m644 xalan.jar "${pkgdir}"/usr/share/java/
  install -m644 xsltc.jar "${pkgdir}"/usr/share/java/
}
