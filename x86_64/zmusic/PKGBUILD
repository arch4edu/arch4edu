# Maintainer: Jan Cholasta <grubber at grubber cz>
pkgname=zmusic
pkgver=1.1.14
pkgrel=1
pkgdesc="GZDoom's music system as a standalone library"
arch=('x86_64' 'aarch64')
url='https://github.com/ZDoom/ZMusic'
license=('BSD' 'GPL3' 'LGPL2.1' 'LGPL3' 'custom:dumb')
depends=('alsa-lib' 'libsndfile' 'mpg123')
optdepends=('soundfont-fluid: default soundfont for FluidSynth')
makedepends=('cmake' 'git')
source=("${pkgname}::git+https://github.com/ZDoom/ZMusic#tag=${pkgver}"
        '0001-Use-correct-soundfont-path.patch')
sha256sums=('SKIP'
            '6c1b5bf589e5c36186869276ade865d35fdf860241dcd2e0f557e5a82dfd066f')

# pkgver() {
#   cd "$pkgname"
  #git describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
#}

prepare() {
    cd "$pkgname"
    patch -i "$srcdir"/0001-Use-correct-soundfont-path.patch -p 1
}

build() {
    cd "$pkgname"
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
    cd "$pkgname"
    make -C build install DESTDIR="$pkgdir"
    install licenses/{bsd,dumb,legal,zmusic}.txt -t "$pkgdir"/usr/share/licenses/$pkgname -D -m 644
}
