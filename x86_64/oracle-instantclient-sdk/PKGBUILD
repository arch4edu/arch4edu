# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sdk
pkgname=oracle-${_pkgname}
pkgver=23.6.0.24.10
_pkgver_vendor_suffix=
_urlver=2360000
_unzippath=instantclient_23_6
pkgrel=1
pkgdesc="Additional header files for developing Oracle applications with Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sdk')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('856abb1333879625b8ed41ccda1bbd82')
sha256sums=('9f7cda57908cf0a5e407da906a86410b22c6d91bee380c4ce585c26e6ec270c7')

package() {
	# Put all .h files into /usr/include
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/include"
	install -m 644 -t "$pkgdir/usr/include" sdk/include/*.h
	# But we don't want this one, it is unused and it conflicts with another
	rm "$pkgdir/usr/include/ldap.h"

	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
