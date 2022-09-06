# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh <skipper13@archlinux.org.ua>
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Viliam Pucik <viliam.pucik@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-odbc
pkgname=oracle-${_pkgname}
pkgver=21.7.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=217000
_unzippath=instantclient_21_7
pkgrel=1
pkgdesc="Additional libraries for enabling ODBC applications with Instant Client"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=(oracle-instantclient-basic=$pkgver)
replaces=('instantclient-odbc')
options=(!strip)

source=("https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('b3c05d4dd6e443f0e502c9229f3d1d66')
sha256sums=('1d3ff37f7cd3c98758486df21afafdbd58fafea9eb8ee43b0c2ebc9701bfb91b')

package() {
	local basedir="$srcdir/${_unzippath}"

	install -d "$pkgdir/usr/lib"
	# Copy files but not symlinks
	install -m 755 -t "$pkgdir/usr/lib" `find "$basedir" -type f -name '*.so*'`

	install -d "$pkgdir/usr/share/oracle"
	install -m 755 -t "$pkgdir/usr/share/oracle" "$basedir/"*.sh

	install -d "$pkgdir/usr/share/doc/oracle"
	install -m 644 -t "$pkgdir/usr/share/doc/oracle" "$basedir/"*README*

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
