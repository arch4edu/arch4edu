# Maintainer: Aaron Keesing <agkphysics at gmail dot com>
# Contributor: Boohbah <boohbah at gmail.com>
# Contributor: Petron <i at jingbei.li>
# Contributor: jzombi <jzombi at gmail.com>

pkgname=opensmile
pkgver=3.0.2
pkgrel=2
pkgdesc="A fast, real-time (audio) feature extraction utility for automatic speech, music and paralinguistic recognition research"
arch=('x86_64')
url="https://github.com/audeering/opensmile/"
license=('custom')
depends=('portaudio' 'ffmpeg4.4')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/audeering/opensmile/archive/v$pkgver.tar.gz")
sha256sums=('b423c785c948e6e8d5b84c002419875ba456f048f5f86ce29f5e21bba9ef5bdd')

prepare() {
  export PKG_CONFIG_PATH="/usr/lib/ffmpeg4.4/pkgconfig/"
}

build() {
  cmake -B build \
    -S "$srcdir/$pkgname-$pkgver" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DSTATIC_LINK=ON \
    -DMARCH_NATIVE=ON \
    -DWITH_PORTAUDIO=ON \
    -DWITH_FFMPEG=ON \
    -DBUILD_FLAGS="-DBUILD_LIBSVM -DBUILD_RNN -DBUILD_SVMSMO" \
    -Wno-dev
  make -C build
}

package() {
  make -C build DESTDIR="$pkgdir" install

  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p "$pkgdir/usr/share/$pkgname"
  cp -a config "$pkgdir/usr/share/$pkgname"
  find "$pkgdir/usr/share/$pkgname/config" -type d -exec chmod 755 {} \;
  find "$pkgdir/usr/share/$pkgname/config" -type f -exec chmod 644 {} \;
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
