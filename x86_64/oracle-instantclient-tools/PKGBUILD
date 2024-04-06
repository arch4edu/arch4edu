# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-tools
pkgname=oracle-${_pkgname}
pkgver=21.13.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=2113000
_unzippath=instantclient_21_13
pkgrel=1
pkgdesc="Data Pump, SQL*Loader and Workload Replay Client for Oracle Instant Client"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('7dd8c74eeb529db848beb08466cd341d')
sha256sums=('5b9e4401580f7bd7fda777df12d5437d80af14cf3838ddd152badea68498fa1b')

package() {
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -d "$pkgdir/usr/share/doc/oracle"
	install -m 755 -t "$pkgdir/usr/bin" exp expdp imp impdp sqlldr wrc
	install -m 755 -t "$pkgdir/usr/lib" *.so*
	install -m 644 -t "$pkgdir/usr/share/doc/oracle" *README*

	# Avoid conflict with WINE
	mv "$pkgdir/usr/bin/wrc" "$pkgdir/usr/bin/wrc-oracle"
}
