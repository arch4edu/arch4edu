# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pkgname=doulos
pkgname=ttf-sil-$_pkgname
_fname=${_pkgname^}SIL
pkgver=6.001
pkgrel=1
pkgdesc='complete support for the International Phonetic Alphabet'
arch=(any)
url="https://software.sil.org/$_pkgname"
license=(OFL)
conflicts=('ttf-sil-fonts<=6')
source=("http://software.sil.org/downloads/r/$_pkgname/$_fname-$pkgver.zip")
sha256sums=('b212d6df691766996c36883dd8e2fc1497cdc4e66a7b52de2d5446d3e763c518')

package() {
	cd "$_fname-$pkgver"
	install -Dm644 -t "$pkgdir/usr/share/fonts/TTF/" *.ttf
	install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" README.txt FONTLOG.txt documentation/pdf/*.pdf
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" OFL.txt
}
