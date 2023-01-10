# Maintainer: Michał Przybyś <michal@przybys.eu>
pkgname=spek
pkgver=0.8.5
pkgrel=1
pkgdesc='An acoustic spectrum analyser'
arch=(x86_64)
url='http://spek.cc/'
license=(GPL3)
depends=(ffmpeg wxwidgets-gtk3)
source=("https://github.com/alexkay/spek/archive/v${pkgver}.tar.gz")
sha256sums=('9053d2dec452dcde421daa0f5f59a9dee47927540f41d9c0c66800cb6dbf6996')

build() {
    cd "spek-${pkgver}"
    export CXXFLAGS="$(pkg-config --cflags-only-I libavutil)"
    ./autogen.sh --with-wx-config=/usr/bin/wx-config --prefix=/usr
    make
}

package() {
    cd "spek-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
