# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-odbc
pkgname=oracle-${_pkgname}
pkgver=23.6.0.24.10
_pkgver_vendor_suffix=
_urlver=2360000
_unzippath=instantclient_23_6
pkgrel=2
pkgdesc="Additional libraries for enabling ODBC applications with Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-odbc')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('39df3b3b21812d2ba7b0f31d488b3663')
sha256sums=('d15465c5149f2dd0b5bad551c7759e6776b109be9d79d697a6ae6da1b738ee71')

package() {
	local basedir="$srcdir/${_unzippath}"

	install -d "$pkgdir/usr/lib"
	# Copy files but not symlinks
	install -m 755 -t "$pkgdir/usr/lib" `find "$basedir" -type f -name '*.so*'`

	install -d "$pkgdir/usr/share/oracle"
	install -m 755 -t "$pkgdir/usr/share/oracle" "$basedir/"*.sh

	install -d "$pkgdir/usr/share/doc/oracle"
	install -m 644 -t "$pkgdir/usr/share/doc/oracle" "$basedir/"*README*

	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "$basedir/"*LICENSE

	# create required symlinks
	cd "$pkgdir/usr/lib" || return 1
	local lib link
	for lib in *.so*; do
		link=$lib
		while [[ ${link#*.} != so ]]; do
			link=${link%.*}
			ln -s $lib $link
		done
	done

}
