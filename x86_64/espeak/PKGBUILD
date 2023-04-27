# Maintainer: SanskritFritz (gmail)
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Mateusz Herych <heniekk@gmail.com>
# Contributor: Christoph Siegenthaler <csi@gmx.ch>

pkgname=espeak
pkgver=1.48.04
pkgrel=4
epoch=1
pkgdesc='Text to Speech engine for English, with support for other languages'
arch=('i686' 'x86_64')
url='http://espeak.sourceforge.net/'
license=('GPL')
depends=('portaudio' 'libpulse')
options=('!emptydirs')
source=("https://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver-source.zip")
sha256sums=('bf9a17673adffcc28ff7ea18764f06136547e97bbd9edf2ec612f09b207f0659')

build() {
  cd "$pkgname-$pkgver-source/src"

  cp portaudio19.h portaudio.h
  make CXXFLAGS="$CXXFLAGS -w -std=c++98" AUDIO=pulseaudio
}

package() {
  cd "$pkgname-$pkgver-source/src"

  make DESTDIR="$pkgdir" install
  chmod 644 "$pkgdir/usr/lib/libespeak.a"
}

# vim:set ts=2 sw=2 et:
