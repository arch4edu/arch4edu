# Maintainer: Martchus <martchus@gmx.net>
# Contributor: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Ben Duffield <bavardage AT archlinux.us>

pkgname=pocketsphinx
pkgver=5.0.0
pkgrel=1
pkgdesc='A small speech recognizer'
arch=('i686' 'x86_64')
url='https://cmusphinx.github.io'
license=('custom')
makedepends=('cmake' 'ninja' 'gst-plugins-base-libs')
optdepends=('gst-plugins-base-libs: GStreamer plugin')
source=("https://github.com/cmusphinx/pocketsphinx/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('78ffe5b60b6981b08667435dd26c5a179b612b8ca372bd9c23c896a8b2239a20')

build() {
  cd "$pkgname-$pkgver"

  cmake -S . -B build -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON -DBUILD_GSTREAMER=ON
  cmake --build build
}

package() {
  cd "$pkgname-$pkgver"

  DESTDIR=${pkgdir} cmake --build build --target install

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
  install -D -m644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
