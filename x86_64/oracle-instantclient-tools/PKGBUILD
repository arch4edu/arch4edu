# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-tools
pkgname=oracle-${_pkgname}
pkgver=23.26.3.0.0
_pkgver_vendor_suffix=
_urlver=2326300
_unzippath=instantclient_23_26
pkgrel=1
pkgdesc="Data Pump, SQL*Loader and Workload Replay Client for Oracle Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('30daa225e893ffad45926c573ac71f7b')
sha256sums=('680b6e6f3b7ae13972d4c3959b3dc4f3bd075a0bed51e5d5b21915d5535f350b')

package() {
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -d "$pkgdir/usr/share/doc/oracle"
	install -m 755 -t "$pkgdir/usr/bin" exp expdp imp impdp sqlldr wrc
	install -m 755 -t "$pkgdir/usr/lib" *.so*
	install -m 644 -t "$pkgdir/usr/share/doc/oracle" *README*
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE

	# Avoid conflict with WINE
	mv "$pkgdir/usr/bin/wrc" "$pkgdir/usr/bin/wrc-oracle"
}
