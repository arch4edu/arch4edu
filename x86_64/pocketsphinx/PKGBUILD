# Maintainer: Martchus <martchus@gmx.net>
# Contributor: éclairevoyant
# Contributor: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Ben Duffield <bavardage AT archlinux.us>

pkgname=pocketsphinx
pkgver=5.0.2
pkgrel=1
pkgdesc='A small speech recognizer'
arch=('i686' 'x86_64')
url='https://cmusphinx.github.io'
license=('BSD' 'MIT')
makedepends=('cmake' 'ninja' 'gst-plugins-base-libs')
optdepends=('gst-plugins-base-libs: GStreamer plugin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/cmusphinx/pocketsphinx/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('c2c58aa702195c46c44575fb9ed5790e749ab647df648b4557cc963aeac638b2')

prepare() {
  cd $pkgname-$pkgver

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
