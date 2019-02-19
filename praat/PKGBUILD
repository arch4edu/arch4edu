# Maintainer:  mrxx <mrxx at cyberhome dot at>
# Contributor: Charlotte Van Petegem <charlotte at vanpetegem dot me>
# Contributor: jpate <jkpate@jkpate.net>

pkgname=praat
pkgver=6.0.48
pkgrel=1
pkgdesc="Doing Phonetics by computer (speech analysis)"
arch=('x86_64')
url="http://www.fon.hum.uva.nl/praat/"
license=('GPL')
depends=('alsa-lib' 'gtk2' 'libpulse' 'jack')
makedepends=('pkg-config' 'gtk2' 'alsa-lib')
optdepends=( 'ttf-sil-fonts' )
conflicts=('praat-bin' 'praat-git')
source=("https://github.com/$pkgname/$pkgname/archive/v$pkgver.tar.gz" "$pkgname.desktop" "$pkgname.xpm" "$pkgname.svg" "$pkgname.1")
sha256sums=('1cd477dd1df49675183e36977c3b6e7840c0e43a1abd0d584278f394fcd93157'
            '94720aedc8e9c9e9d53b3230d79ccaae551b5bc5e6986528664311d55f3cce5a'
            '07abf61475f22f83f0514a8fba1ec7bd3821d2b7f35b1215c1f3e1feb947d74b'
            'db6c7568f6e13b4ce7c37bd9fcf289832867f79ba7d7fc48c4f13f0045ad98f1'
            '21ee03cae45be634c57c167c2dfbdfd9d9b7feadb98e0124413d9426c199e81c')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  cp "makefiles/makefile.defs.linux.pulse" "makefile.defs"
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make
}

package() {
  mkdir -p -m 755 $pkgdir/usr/share/{applications,icons/hicolor/scalable/apps,man/man1,pixmaps}
  install -Dm755  "$srcdir/$pkgname-$pkgver/praat" "$pkgdir/usr/bin/praat"
  install -Dm644 "$srcdir/${pkgname}.desktop" "$pkgdir/usr/share/applications/"
  install -Dm644 "$srcdir/${pkgname}.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/"
  install -Dm644 "$srcdir/${pkgname}.xpm" "$pkgdir/usr/share/pixmaps/"
  install -m644 "${pkgname}.1" "${pkgdir}/usr/share/man/man1/"
}
