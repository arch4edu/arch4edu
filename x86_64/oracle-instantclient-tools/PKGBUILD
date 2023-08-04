# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-tools
pkgname=oracle-${_pkgname}
pkgver=21.11.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=2111000
_unzippath=instantclient_21_11
pkgrel=1
pkgdesc="Data Pump, SQL*Loader and Workload Replay Client for Oracle Instant Client"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('4f7936e593db380829f70209dbb51595')
sha256sums=('b8066f097a3fa5921bcec81364c210bd2ab75031125fdbe2122f4443dd676eb0')

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
