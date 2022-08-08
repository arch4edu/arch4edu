# Maintainer: Michał Przybyś <michal@przybys.eu>
pkgname=spek
pkgver=0.8.4
pkgrel=2
pkgdesc='An acoustic spectrum analyser'
arch=(x86_64)
url='http://spek.cc/'
license=(GPL3)
depends=(ffmpeg4.4 wxwidgets-gtk3)
source=("https://github.com/alexkay/spek/archive/v${pkgver}.tar.gz")
sha256sums=(1751246e958cff91fe30b01925a38bf8cbd9c6abbd0d24e5b21eaad3d054534b)

build() {
    cd "spek-${pkgver}"
    export PKG_CONFIG_PATH=/usr/lib/ffmpeg4.4/pkgconfig
    export CXXFLAGS="$(pkg-config --cflags-only-I libavutil)"
    ./autogen.sh --with-wx-config=/usr/bin/wx-config --prefix=/usr
    make
}

package() {
    cd "spek-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
