# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pkgname=doulos
pkgname=ttf-sil-$_pkgname
_fname=${_pkgname^}SIL
pkgver=6.200
pkgrel=1
pkgdesc='complete support for the International Phonetic Alphabet'
arch=(any)
url="https://software.sil.org/$_pkgname"
license=(OFL-1.1-RFN)
source=("http://software.sil.org/downloads/r/$_pkgname/$_fname-$pkgver.zip")
sha256sums=('a7ad76326c126b2748297b987a634a56f7e42cd45bc3ff2c90a7909cbb164223')

package() {
	cd "$_fname-$pkgver"
	install -Dm644 -t "$pkgdir/usr/share/fonts/TTF/" *.ttf
	install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" README.txt FONTLOG.txt documentation/pdf/*.pdf
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" OFL.txt
}
