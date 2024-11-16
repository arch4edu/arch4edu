# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-sqlplus
pkgname=oracle-${_pkgname}
pkgver=23.6.0.24.10
_pkgver_vendor_suffix=
_urlver=2360000
_unzippath=instantclient_23_6
pkgrel=1
pkgdesc="SQL*Plus for Oracle Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-sqlplus')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('08c8c6a4e41a1299eeeccb20e853e0b9')
sha256sums=('20fcc3a1df794a0b4032c2ae9562e191872d033aabf0dcd2e673b28c4a93ccef')

package() {
	cd "$srcdir/${_unzippath}"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" sqlplus
	install -m 755 -t "$pkgdir/usr/lib" *.so
	install -m 644 -t "$pkgdir/usr/lib" *.sql
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" *LICENSE
}
