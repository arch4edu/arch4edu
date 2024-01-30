# Maintainer: Jan Cholasta <grubber at grubber cz>
# Contributor: Christoph Zeiler <rabyte*gmail>

pkgname=gzdoom
pkgver=4.11.3
pkgrel=2
pkgdesc='Feature centric port for all Doom engine games'
arch=('i686' 'x86_64' 'aarch64')
url='http://www.zdoom.org/'
license=('BSD' 'GPL3' 'LGPL3')
depends=('gtk3'
         'hicolor-icon-theme'
         'libgl'
         'libvpx>=1.14'
         'libwebp'
         'openal'
         'sdl2'
         'zmusic>=1.1.8')
makedepends=('cmake' 'desktop-file-utils' 'git')
optdepends=('blasphemer-wad: Blasphemer (free Heretic) game data'
            'chexquest3-wad: Chex Quest 3 game data'
            'doom1-wad: Doom shareware game data'
            'freedm: FreeDM game data'
            'freedoom: Freedoom game data'
            'gxmessage: crash dialog (GNOME)'
            'hacx-wad: HacX game data'
            'harmony-wad: Harmony game data'
            'heretic1-wad: Heretic shareware game data'
            'hexen1-wad: Hexen demo game data'
            'kdialog: crash dialog (KDE)'
            'strife0-wad: Strife shareware game data'
            'square1-wad: The Adventures of Square, Episode 1 game data'
            'urbanbrawl-wad: Urban Brawl: Action Doom 2 game data'
            'xorg-xmessage: crash dialog (other)')
optdepends_x86_64=('vulkan-driver: Vulkan renderer'
                   'vulkan-icd-loader: Vulkan renderer')
replaces=('gzdoom1' 'gzdoom-legacy')
options=(!lto)
source=("gzdoom::git+https://github.com/coelckers/gzdoom.git#tag=g${pkgver}"
        'gzdoom.desktop'
        '0001-Fix-file-paths.patch')
sha256sums=('SKIP'
            '59122e670f72aa2531aff370e7aaab2d886a7642e79e91f27a533d3b4cad4f6d'
            'a37dde8274e1a9fd511af951da2e362d503ab4be72e79d4843e1ca3a0129549f')

prepare() {
    cd gzdoom
    patch -i "$srcdir"/0001-Fix-file-paths.patch -p 1
}

build() {
    cd gzdoom
    mkdir -p build
    cmake -B build \
          -D CMAKE_BUILD_TYPE=Release \
          -D CMAKE_CXX_FLAGS="$CXXFLAGS -ffile-prefix-map=\"$PWD\"=. -DSHARE_DIR=\\\"/usr/share/gzdoom\\\"" \
          -D CMAKE_INSTALL_PREFIX=/usr \
          -D SYSTEMINSTALL=ON \
          -D INSTALL_PK3_PATH=share/gzdoom \
          -D INSTALL_SOUNDFONT_PATH=share/gzdoom \
          -D INSTALL_RPATH=/usr/lib \
          -D DYN_GTK=OFF \
          -D DYN_OPENAL=OFF
    make -C build
}

package() {
    cd gzdoom
    make -C build install DESTDIR="$pkgdir"
    install -d "$pkgdir"/usr/share/licenses
    mv "$pkgdir"/usr/share/doc/gzdoom/licenses "$pkgdir"/usr/share/licenses/gzdoom
    desktop-file-install "$srcdir"/gzdoom.desktop --dir="$pkgdir"/usr/share/applications
    install src/posix/zdoom.xpm -D -m 644 "$pkgdir"/usr/share/icons/hicolor/256x256/apps/gzdoom.xpm
}
