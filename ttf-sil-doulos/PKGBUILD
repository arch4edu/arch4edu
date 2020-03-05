# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pkgname=doulos
pkgname=ttf-sil-$_pkgname
_fname=${_pkgname^}SIL
pkgver=5.000
pkgrel=4
pkgdesc='complete support for the International Phonetic Alphabet'
arch=('any')
url="https://software.sil.org/$_pkgname"
license=('OFL')
conflicts=('ttf-sil-fonts<=6')
source=("http://software.sil.org/downloads/r/$_pkgname/$_fname-$pkgver.zip")
sha256sums=('0b309c3db813a98ce884c0bd25c7f5c0bd96bbffd076459e39298812ca22472e')

package() {
    cd "$_fname-$pkgver"
    find -type f -name "$_fname*.ttf" -execdir \
        install -Dm644 -t "$pkgdir/usr/share/fonts/TTF" {} \;
    install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" README.txt FONTLOG.txt documentation/*.pdf
    install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" OFL.txt
}
