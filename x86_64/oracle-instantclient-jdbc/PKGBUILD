# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-jdbc
pkgname=oracle-${_pkgname}
pkgver=23.6.0.24.10
_pkgver_vendor_suffix=
_urlver=2360000
_unzippath=instantclient_23_6
pkgrel=1
pkgdesc="Additional support for XA, Internationalization, and RowSet operations under JDBC"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-jdbc')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('aaae817e05677679f16cb128707f51c7')
sha256sums=('c1060996d5ec8e823bc67bd35eefe6c07d2f926fe183ef8ee037716d82e54b81')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.jar
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
