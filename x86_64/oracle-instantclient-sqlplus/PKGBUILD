# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sqlplus
pkgname=oracle-${_pkgname}
pkgver=23.5.0.24.07
_pkgver_vendor_suffix=
_urlver=2350000
_unzippath=instantclient_23_5
pkgrel=1
pkgdesc="SQL*Plus for Oracle Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('f164658cf40f5c912c8c5cf1141fe864')
sha256sums=('9ffb7c65209cdfdf3601e70e7b8e3bf6e0cb52a995922f88cc8fd326c55796a9')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" sqlplus
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.sql
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
