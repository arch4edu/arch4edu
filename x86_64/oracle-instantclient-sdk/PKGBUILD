# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sdk
pkgname=oracle-${_pkgname}
pkgver=21.11.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=2111000
_unzippath=instantclient_21_11
pkgrel=1
pkgdesc="Additional header files for developing Oracle applications with Instant Client"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sdk')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('07bcb9525937706824ba5db39dcd61be')
sha256sums=('c4dc168fee1bc759e4f87c8bc10a7d949dd51b5f218fee997cac6a76602967c4')

package() {
	# Put all .h files into /usr/include
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/include"
	install -m 644 -t "$pkgdir/usr/include" sdk/include/*.h
	# But we don't want this one, it is unused and it conflicts with another
	rm "$pkgdir/usr/include/ldap.h"
}
