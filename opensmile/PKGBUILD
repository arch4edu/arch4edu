# Maintainer: Boohbah <boohbah at gmail.com>
# Contributor: Petron <i at jingbei.li>
# Contributor: jzombi <jzombi at gmail.com>

pkgname=opensmile
pkgver=2.2rc1
pkgrel=2
pkgdesc="A fast, real-time (audio) feature extraction utility for automatic speech, music and paralinguistic recognition research"
arch=('i686' 'x86_64')
url="http://www.audeering.com/research/opensmile"
license=('custom')
depends=('portaudio')
source=("http://www.audeering.com/research-and-open-source/files/openSMILE-$pkgver.tar.gz")
md5sums=('d041c32af5e11e344a3daa7d923917cf')

build() {
  cd "openSMILE-$pkgver"
  ./autogen.sh
  ./autogen.sh
  ./configure \
    --prefix="/usr" --with-portaudio="yes" \
    CXXFLAGS="-O2 -mfpmath=sse -march=native -Wno-narrowing"
  make
}

package() {
  cd "openSMILE-$pkgver"
  make DESTDIR="$pkgdir" install
  mkdir -p "$pkgdir/usr/share/$pkgname"
  cp -a config "$pkgdir/usr/share/$pkgname"
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}

# vim:set ts=2 sw=2 et:
