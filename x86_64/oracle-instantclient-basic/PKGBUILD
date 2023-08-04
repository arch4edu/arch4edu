# Contributor: Adam Nielsen <malvineous@shikadi.net>
# Contributor: Vitaliy Berdinskikh ur6lad[at]archlinux.org.ua
# Contributor: Andrea Agosti <cifvts@gmail.com>
# Contributor: Charles Clement <caratorn@gmail.com>
# Contributor: Geraldo Augusto Vecchiato <geraldoav@gmail.com>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

_pkgname=instantclient-basic
pkgname=oracle-${_pkgname}
pkgver=21.11.0.0.0
_pkgver_vendor_suffix=dbru
_urlver=2111000
_unzippath=instantclient_21_11
pkgrel=1
pkgdesc="Light replacement for the Oracle client (files to run OCI, OCCI and JDBC-OCI programs)"
arch=('x86_64')
url="http://www.oracle.com/technetwork/database/features/instant-client/"
license=('custom:OTN')
depends=('gcc-libs' 'libaio')
replaces=('instantclient-basic' 'instantclient-basiclite')
options=(!strip)

# These are the only files we want to include in the source package
source=(LICENSE
        oracle.sh
        "https://download.oracle.com/otn_software/linux/instantclient/${_urlver}/${_pkgname}-linux.x64-${pkgver}${_pkgver_vendor_suffix}.zip")
md5sums=('2d62e22e4f2d7e6d220fafde0f692a7d'
         '784005aa31cb56bb2303179d98fccd8e'
         '12facf30f567c7d75e789bf59148f294')
sha256sums=('f904a30b07ddf7806a33620f93b94c3d315154d26a371ece48695bb3555064a2'
            '36b5ab97950f1667403dd9b59c3cad25d8f9e457702feaece835d1bff7c971c9'
            'fd18de92caac2586fa4ef1d267902f527a67236989f3284bd32d644f83ed2a29')

package() {
	cd "$srcdir/${_unzippath}/"
	install -d "$pkgdir/usr/bin"
	install -d "$pkgdir/usr/lib"
	install -m 755 -t "$pkgdir/usr/bin" adrci genezi uidrvci
	# Copy files but not symlinks
	install -m 755 -t "$pkgdir/usr/lib" `find . -type f -name '*.so*'`
	install -m 644 -t "$pkgdir/usr/lib" *.jar

	# Copy across the script to set environment variables
	install -Dm755 "$srcdir/oracle.sh" "$pkgdir/etc/profile.d/oracle.sh"

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

	install -Dm644 "$srcdir/LICENSE" \
		"$pkgdir/usr/share/licenses/$pkgname/LICENSE" || return 1
}
