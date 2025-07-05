# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Anton Kudelin <kudelin at proton dot me>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Andya <hugo981@gmx.com>
# Contributor: Lazaros Koromilas <koromilaz@gmail.com>
_base=Saxon-HE
pkgname=${_base,,}
pkgver=12.8
pkgrel=1
arch=(any)
pkgdesc="XSLT 3.0, XQuery 3.1, and XPath 3.1 processor for Java - Home Edition"
url="https://github.com/Saxonica/${_base}"
license=(MPL-2.0)
depends=(java-runtime-headless)
provides=(java-saxon)
conflicts=(java-saxon)
source=(${url}/releases/download/${_base/-/}-${pkgver//./-}/${_base/-/}${pkgver//./-}J.zip
  saxon-xslt.sh
  saxon-xquery.sh)
sha512sums=('643aee8098b198d042acba28f3ca98ec191eb2489b8bc05d5a8ffdffac6ca8a21c34d6189b07b63dd75213af5aca1b45f13432827def1a3773e63afd078e47f9'
            '365eba91dc83600231b1c54c427eca9e076003ed9204c37fe5da777443d190afb22bdc45c305e16181f2738254f6e016a136d9688ddb2d47a6de873245f64f21'
            'b44d1ea24ae6f1e0d34cf86ecc3c83642e2ed3c89230683cc04c7c8992e3a2fc9f191bb565437700a2dcbb56980bbb3c0540e628ad28df43095688da344a9429')

package() {
  install -Dm644 $pkgname-$pkgver.jar "$pkgdir/usr/share/java/saxon/$pkgname-$pkgver.jar"
  install -Dm755 saxon-xquery.sh "${pkgdir}"/usr/bin/saxon-xquery
  install -Dm755 saxon-xslt.sh "${pkgdir}"/usr/bin/saxon-xslt

  # link with simpler name for compat with others
  ln -s $pkgname-$pkgver.jar "${pkgdir}"/usr/share/java/saxon/saxon.jar
  ln -s saxon-xslt "$pkgdir/usr/bin/saxon"
}
