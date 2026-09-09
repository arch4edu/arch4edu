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
# Then run `pacman -Sy` then `pacman -S oracle-instantclient-sqlplus`

_pkgname=instantclient-sqlplus
pkgname=oracle-${_pkgname}
pkgver=23.26.3.0.0
_pkgver_vendor_suffix=
_urlver=2326300
_unzippath=instantclient_23_26
pkgrel=1
pkgdesc="SQL*Plus for Oracle Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('0e63f3c8644798ba37915c29a3006c0a')
sha256sums=('6570d7939856767cdbb549b51e1423d6a5f53143c57c30c015669706f65a632a')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" sqlplus
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.sql
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
