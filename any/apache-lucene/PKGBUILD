# Maintainer: Jingbei Li <i@jingbei.li>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>

_pkgname=lucene
pkgname=apache-$_pkgname
pkgver=10.3.2
pkgrel=1
pkgdesc="Apache Lucene is a high-performance, full-featured text search engine library written entirely in Java."
arch=('any')
url="https://lucene.apache.org/"
license=('Apache')
depends=('java-runtime')
source=("https://downloads.apache.org/$_pkgname/java/$pkgver/$_pkgname-$pkgver.tgz")
sha256sums=('ad6064be247a4ac80f05c585c98354ab6fc447bb0c4b1fda925feee00fdbb627')

package() {
	cd "${srcdir}/$_pkgname-$pkgver"
	mkdir -p $pkgdir/usr/share/java/$pkgname
	find . -type f -not \( -path '*test-framework*' -prune \) -name '*.jar' -exec mv {} $pkgdir/usr/share/java/$pkgname \;
	install -Dm644 "LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

	find licenses/ -type f -name '*.txt' -exec install -Dm644 {} "${pkgdir}/usr/share/licenses/${pkgname}/" \;
	sed -i 's|$MODULES/modules:$MODULES/modules-thirdparty|/usr/share/java/apache-lucene/|g' bin/luke.sh
	install -Dm755 bin/luke.sh "${pkgdir}/usr/bin/luke"
}
