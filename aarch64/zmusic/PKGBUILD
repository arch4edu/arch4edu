# Maintainer: Jan Cholasta <grubber at grubber cz>
pkgname=zmusic
pkgver=1.1.13
pkgrel=1
pkgdesc="GZDoom's music system as a standalone library"
arch=('x86_64' 'aarch64')
url='https://github.com/coelckers/ZMusic'
license=('BSD' 'GPL3' 'LGPL2.1' 'LGPL3' 'custom:dumb')
depends=('alsa-lib' 'libsndfile' 'mpg123')
optdepends=('soundfont-fluid: default soundfont for FluidSynth')
makedepends=('cmake')
_srcname=ZMusic-${pkgver}
source=("${_srcname}.tar.gz::https://github.com/coelckers/ZMusic/archive/${pkgver}.tar.gz"
        '0001-Use-correct-soundfont-path.patch')
sha256sums=('564e210837b653013e01d67f04d0d906a9f0a923521e0c305463ec4f4a139ed4'
            '6c1b5bf589e5c36186869276ade865d35fdf860241dcd2e0f557e5a82dfd066f')

prepare() {
    cd $_srcname
    patch -i "$srcdir"/0001-Use-correct-soundfont-path.patch -p 1
}

build() {
    cd $_srcname
    mkdir -p build
    cmake -B build \
          -D CMAKE_BUILD_TYPE=Release \
          -D CMAKE_INSTALL_PREFIX=/usr \
          -D CMAKE_C_FLAGS="${CFLAGS} -ffile-prefix-map=\"${PWD}\"=." \
          -D CMAKE_CXX_FLAGS="${CXXFLAGS} -ffile-prefix-map=\"${PWD}\"=." \
          -D DYN_MPG123=OFF \
          -D DYN_SNDFILE=OFF
    make -C build
}

package() {
    cd $_srcname
    make -C build install DESTDIR="$pkgdir"
    install licenses/{bsd,dumb,legal,zmusic}.txt -t "$pkgdir"/usr/share/licenses/$pkgname -D -m 644
}
