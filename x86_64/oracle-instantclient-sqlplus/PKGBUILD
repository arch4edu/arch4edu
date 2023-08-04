# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sqlplus
pkgname=oracle-${_pkgname}
pkgver=21.11.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=2111000
_unzippath=instantclient_21_11
pkgrel=1
pkgdesc="SQL*Plus for Oracle Instant Client"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('273877433bb203f2af7e8e4e89b154d5')
sha256sums=('8a0544db6ce28d41a91693c720422a136684dc5927cea050128c175f385810a7')

package() {
	local basedir="$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" "$basedir/sqlplus"
	install -m 755 -t "$pkgdir/usr/lib" "$basedir/"*.so
	install -m 644 -t "$pkgdir/usr/lib" "$basedir/"*.sql
}
