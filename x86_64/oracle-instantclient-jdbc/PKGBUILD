# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-jdbc
pkgname=oracle-${_pkgname}
pkgver=23.5.0.24.07
_pkgver_vendor_suffix=
_urlver=2350000
_unzippath=instantclient_23_5
pkgrel=2
pkgdesc="Additional support for XA, Internationalization, and RowSet operations under JDBC"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-jdbc')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('aee2639b45799e1061233de7e022df43')
sha256sums=('8e7b97fbddda86ccdb122a4690001ba10eddfc746fab34ae19d4944d3cb298d9')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.jar
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
