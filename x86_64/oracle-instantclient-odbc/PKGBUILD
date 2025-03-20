# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-odbc
pkgname=oracle-${_pkgname}
pkgver=23.7.0.25.01
_pkgver_vendor_suffix=
_urlver=2370000
_unzippath=instantclient_23_7
pkgrel=1
pkgdesc="Additional libraries for enabling ODBC applications with Instant Client"
arch=('x86_64')
url="https://www.oracle.com/at/database/technologies/instant-client/downloads.html"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-odbc')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('4ba531e995a95d02a463fa99b785df0f')
sha256sums=('7015edc632dcfed93d7ac11551ae5b4f07a23a81be312df6fea729bec2e3eb18')

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
