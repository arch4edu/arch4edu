# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

# This package is also available as a Pacman repo, to simplify upgrades.
# Add the following lines to the end of /etc/pacman.conf:
#
# [oracle]
# SigLevel = Optional TrustAll
# Server = http://linux.shikadi.net/arch/$repo/$arch/
#
# Then run `pacman -Sy` then `pacman -S oracle-instantclient-sdk`

_pkgname=instantclient-sdk
pkgname=oracle-${_pkgname}
pkgver=23.26.3.0.0
_pkgver_vendor_suffix=
_urlver=2326300
_unzippath=instantclient_23_26
pkgrel=1
pkgdesc="Additional header files for developing Oracle applications with Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sdk')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('8673eabe76f32d3034089abf5831b5cb')
sha256sums=('7ac13587ba8a734ae7cc06cf42753bbfdbe69839daf87bd5935a49c83decccfd')

package() {
	# Put all .h files into /usr/include
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/include"
	install -m 644 -t "$pkgdir/usr/include" sdk/include/*.h
	# But we don't want this one, it is unused and it conflicts with another
	rm "$pkgdir/usr/include/ldap.h"

	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
