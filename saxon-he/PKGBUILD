# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Andya <hugo981@gmx.com>
# Contributor: Lazaros Koromilas <koromilaz@gmail.com>

pkgname=saxon-he
pkgver=10.6
_pkgver=${pkgver//./-}
pkgrel=1
pkgdesc="XSLT 2.0 / XPath 2.0 and 3.0 / XQuery 1.0 and 3.0 processor for Java - Home Edition"
url="http://saxon.sourceforge.net"
license=('MPL')
arch=('any')
depends=('java-runtime-headless')
provides=('java-saxon')
conflicts=('java-saxon')
source=("https://downloads.sourceforge.net/saxon/SaxonHE${_pkgver}J.zip"
        "saxon-xslt.sh"
        "saxon-xquery.sh")
sha256sums=('0e590ede60eef6d8a98e759f72769c20417173f99191ebbc2f9ec4e331dbc296'
            '407e00b19754d21df78e39912d5499e62fa02988374e86c59d8d9e41b3235948'
            'e4e72afa5cc1f8277d9e87acbf51cb3ed734d2d7d3c4a8c28b2bb7d39699830f')

package() {
    cd "$srcdir"
    install -Dm644 $pkgname-$pkgver.jar "$pkgdir/usr/share/java/saxon/$pkgname-$pkgver.jar"
    install -Dm755 saxon-xslt.sh "$pkgdir/usr/bin/saxon-xslt"
    install -Dm755 saxon-xquery.sh "$pkgdir/usr/bin/saxon-xquery"
    # link with simpler name for compat with others
    ln -s $pkgname-$pkgver.jar "$pkgdir/usr/share/java/saxon/saxon.jar"
    ln -s saxon-xslt "$pkgdir/usr/bin/saxon"
}
