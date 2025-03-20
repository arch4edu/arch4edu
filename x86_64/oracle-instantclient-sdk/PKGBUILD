# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sdk
pkgname=oracle-${_pkgname}
pkgver=23.7.0.25.01
_pkgver_vendor_suffix=
_urlver=2370000
_unzippath=instantclient_23_7
pkgrel=1
pkgdesc="Additional header files for developing Oracle applications with Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sdk')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('ba02d7c91586dc35cb8ecd27075a484e')
sha256sums=('1f3a0ff568221662430ad2187db30e99d61c051f715c34b19cbaeff016293604')

package() {
	# Put all .h files into /usr/include
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/include"
	install -m 644 -t "$pkgdir/usr/include" sdk/include/*.h
	# But we don't want this one, it is unused and it conflicts with another
	rm "$pkgdir/usr/include/ldap.h"

	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
