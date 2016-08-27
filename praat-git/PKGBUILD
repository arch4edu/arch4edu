# Maintainer: rmanne <rahul_manne@hotmail.com>
pkgname=praat-git
pkgver=r491.f9a62ee
pkgver() {
    cd "${pkgname%-git}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}
pkgrel=1
pkgdesc="A tool for 'Doing Phonetics by computer'"
arch=('x86_64' 'i686')
url="http://www.fon.hum.uva.nl/praat/"
license=('GPL')
depends=('alsa-lib' 'gtk2')
makedepends=('pkg-config')
optdepends=('ttf-sil-fonts')
provides=('praat')
conflicts=('praat')
source=('praat::git+https://github.com/praat/praat.git')
md5sums=('SKIP')

prepare() {
    cd "$srcdir/${pkgname%-git}"
    cp makefiles/makefile.defs.linux.alsa makefile.defs
}

build() {
    cd "$srcdir/${pkgname%-git}"
    make
}

package() {
    cd "$srcdir/${pkgname%-git}"
    install -Dm755  praat "$pkgdir/usr/bin/praat"
}
