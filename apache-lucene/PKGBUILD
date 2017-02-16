# Maintainer: Jingbei Li <i@jingbei.li>

_pkgname=lucene
pkgname=apache-$_pkgname
pkgver=6.4.1
pkgrel=2
pkgdesc="Apache Lucene is a high-performance, full-featured text search engine library written entirely in Java."
arch=('any')
url="https://lucene.apache.org/"
license=('APACHE')
depends=('java-runtime')
_mirror="http://mirrors.tuna.tsinghua.edu.cn/apache"
source=("$_mirror/$_pkgname/java/$pkgver/$_pkgname-${pkgver}.tgz")
md5sums=('e1354af6e796144e73bf3ab7af1b0bf3')

package() {
	cd "${srcdir}/$_pkgname-$pkgver"
	mkdir -p $pkgdir/usr/share/java/$pkgname
	find . -type f -name '*.jar' -exec mv {} $pkgdir/usr/share/java/$pkgname \;
	install -Dm644 "LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/license.txt"
}
