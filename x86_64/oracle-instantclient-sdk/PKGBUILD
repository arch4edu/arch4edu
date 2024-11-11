# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sdk
pkgname=oracle-${_pkgname}
pkgver=23.5.0.24.07
_pkgver_vendor_suffix=
_urlver=2350000
_unzippath=instantclient_23_5
pkgrel=1
pkgdesc="Additional header files for developing Oracle applications with Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sdk')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('f9c74ab87f6f1f5a461acee4b9725ef3')
sha256sums=('20160c5ddbd68ba37ef594872e610c783bce7c94324fa1b6c1dda9175f66d3db')

package() {
	# Put all .h files into /usr/include
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/include"
	install -m 644 -t "$pkgdir/usr/include" sdk/include/*.h
	# But we don't want this one, it is unused and it conflicts with another
	rm "$pkgdir/usr/include/ldap.h"

	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
