# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sqlplus
pkgname=oracle-${_pkgname}
pkgver=21.13.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=2113000
_unzippath=instantclient_21_13
pkgrel=1
pkgdesc="SQL*Plus for Oracle Instant Client"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('10066ec4d51d02b9c96be3e48d6696de')
sha256sums=('65e12ab0232427312bade2e814d4b01e8018bd8027ff950b2504ece3ac1c39b6')

package() {
	local basedir="$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" "$basedir/sqlplus"
	install -m 755 -t "$pkgdir/usr/lib" "$basedir/"*.so
	install -m 644 -t "$pkgdir/usr/lib" "$basedir/"*.sql
}
