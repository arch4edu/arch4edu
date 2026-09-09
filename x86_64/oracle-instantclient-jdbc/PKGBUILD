# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-jdbc
pkgname=oracle-${_pkgname}
pkgver=23.26.3.0.0
_pkgver_vendor_suffix=
_urlver=2326300
_unzippath=instantclient_23_26
pkgrel=1
pkgdesc="Additional support for XA, Internationalization, and RowSet operations under JDBC"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-jdbc')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('d296799d78f9914f4aca4a2fb0bc38b6')
sha256sums=('8e57710546ebeb03c864882b5f4620ac42ef793c1e72abdcaa277791d2433eac')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.jar
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
