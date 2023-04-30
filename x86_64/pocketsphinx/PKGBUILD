# Maintainer: Martchus <martchus@gmx.net>
# Contributor: éclairevoyant
# Contributor: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Ben Duffield <bavardage AT archlinux.us>

pkgname=pocketsphinx
pkgver=5.0.0
pkgrel=2
pkgdesc='A small speech recognizer'
arch=('i686' 'x86_64')
url='https://cmusphinx.github.io'
license=('BSD' 'MIT')
makedepends=('cmake' 'ninja' 'gst-plugins-base-libs')
optdepends=('gst-plugins-base-libs: GStreamer plugin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/cmusphinx/pocketsphinx/archive/refs/tags/v$pkgver.tar.gz"
        '66685a74bb55d82a97c6ae46b7cd91152bbbfffd.patch')
sha256sums=('78ffe5b60b6981b08667435dd26c5a179b612b8ca372bd9c23c896a8b2239a20'
            '428fc297f047ea95fe24f7e43b723cdfdb7215de518455e939ef86ff1aa10af6')

prepare() {
  cd $pkgname-$pkgver

  patch -p1 -i ../66685a74bb55d82a97c6ae46b7cd91152bbbfffd.patch
}

build() {
  cd $pkgname-$pkgver

  cmake -S . -B build -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON -DBUILD_GSTREAMER=ON
  cmake --build build
}

package() {
  cd $pkgname-$pkgver

  DESTDIR="$pkgdir" cmake --install build

  install -D -m644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
