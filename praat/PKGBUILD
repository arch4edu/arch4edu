# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer:  svkampen <sam at tehsvk dot net>
# Contributor: Charlotte Van Petegem <charlotte at vanpetegem dot me>
# Contributor: jpate <jkpate@jkpate.net>

# See Debian packaging for details, rules and control files linked here:
# https://tracker.debian.org/pkg/praat

# TODO: Build and package praat-nogui and sendpraat, as in Debian.

pkgname=praat
pkgver=6.1.10
pkgrel=1
pkgdesc='Doing Phonetics by computer (speech analysis)'
arch=('x86_64' 'i686')
url='http://www.praat.org/'
license=('GPL')
depends=('alsa-lib' 'gtk2' 'jack' 'libpulse' 'ttf-charis-sil' 'ttf-sil-doulos')
optdepends=('ttf-sil-fonts')
source=("$pkgname-$pkgver.tar.gz::https://github.com/$pkgname/$pkgname/archive/v$pkgver.tar.gz"
        "$pkgname.1"
        "$pkgname.desktop"
        "$pkgname.svg"
        "$pkgname.xpm")
sha256sums=('7b0079d6a17fadc6495aee8827e4641392f6067c299b53b3a16b4cf383ec5b71'
            '21ee03cae45be634c57c167c2dfbdfd9d9b7feadb98e0124413d9426c199e81c'
            '94720aedc8e9c9e9d53b3230d79ccaae551b5bc5e6986528664311d55f3cce5a'
            'db6c7568f6e13b4ce7c37bd9fcf289832867f79ba7d7fc48c4f13f0045ad98f1'
            '07abf61475f22f83f0514a8fba1ec7bd3821d2b7f35b1215c1f3e1feb947d74b')

prepare() {
    cd "$pkgname-$pkgver"
    cp makefiles/makefile.defs.linux.pulse makefile.defs
}

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 -t "$pkgdir/usr/bin" "$pkgname"
    install -Dm644 -t "$pkgdir/usr/share/applications/" "../$pkgname.desktop"
    install -Dm644 -t "$pkgdir/usr/share/icons/hicolor/scalable/apps/" "../$pkgname.svg"
    install -Dm644 -t "$pkgdir/usr/share/pixmaps/" "../$pkgname.xpm"
    install -Dm644 -t "$pkgdir/usr/share/man/man1/" "../$pkgname.1"
}
