# Maintainer: Charlotte Van Petegem <charlotte at vanpetegem dot me>
# Maintainer: jpate <jkpate@jkpate.net>
pkgname=praat
pkgver=6.0.43
pkgrel=2
pkgdesc="A tool for 'Doing Phonetics by computer'"
arch=('x86_64')
url="http://www.fon.hum.uva.nl/praat/"
license=('GPL')
depends=( 'alsa-lib' 'gtk2' 'libpulse' )
makedepends=('pkg-config' 'gtk2' 'alsa-lib')
optdepends=( 'ttf-sil-fonts' )

source=("https://github.com/$pkgname/$pkgname/archive/v$pkgver.tar.gz")

md5sums=('e66aaec26a7753430e933834c5795595')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  cp "makefiles/makefile.defs.linux.pulse" "makefile.defs"
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make
}

package() {
  install -Dm755  "$srcdir/$pkgname-$pkgver/praat" "$pkgdir/usr/bin/praat"
}
