# Maintainer:  Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Andya <hugo981@gmx.com>
# Contributor: Lazaros Koromilas <koromilaz@gmail.com>

pkgname=saxon-he
pkgver=12.3
_pkgver=${pkgver//./-}
pkgrel=1
arch=(any)
pkgdesc="XSLT 3.0, XQuery 3.1, and XPath 3.1 processor for Java - Home Edition"
url="http://saxon.sourceforge.net"
license=(MPL)
depends=(java-runtime-headless)
provides=(java-saxon)
conflicts=(java-saxon)
source=(https://github.com/Saxonica/Saxon-HE/releases/download/SaxonHE${_pkgver}/SaxonHE${_pkgver}J.zip
        saxon-xslt.sh
        saxon-xquery.sh)
sha256sums=('3b69ea2f817cab49072f9e85dae5e01979515f2458844f7334d26025f5ec9418'
            '0ad3cae41f7a351e5311ddea5ac0bc27bb19197f0ce9c552a7aa209864089c2b'
            '00447c1917a5ef5531dfa76d8779e4da21609b4d2b45dbb0dd4227d2299ebde8')

package() {
  cd "$srcdir"
  install -Dm644 $pkgname-$pkgver.jar \
    "$pkgdir/usr/share/java/saxon/$pkgname-$pkgver.jar"
  install -Dm755 saxon-xslt.sh "$pkgdir/usr/bin/saxon-xslt"
  install -Dm755 saxon-xquery.sh "$pkgdir/usr/bin/saxon-xquery"
  # link with simpler name for compat with others
  ln -s $pkgname-$pkgver.jar "$pkgdir/usr/share/java/saxon/saxon.jar"
  ln -s saxon-xslt "$pkgdir/usr/bin/saxon"
}
