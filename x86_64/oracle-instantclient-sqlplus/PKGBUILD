# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sqlplus
pkgname=oracle-${_pkgname}
pkgver=23.26.2.0.0
_pkgver_vendor_suffix=
_urlver=2326200v2
_unzippath=instantclient_23_26
pkgrel=1
pkgdesc="SQL*Plus for Oracle Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('56261bd9d512e7cbdd36a8fe63e47fb8')
sha256sums=('5d3c916c0b7ff761d157edfb8da526b410a9cf40e3f01c02ea22c2654764d5f5')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" sqlplus
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.sql
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
