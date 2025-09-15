pkgname=fheroes2
pkgver=1.1.11
pkgrel=1
pkgdesc="Recreation of the Heroes of Might and Magic II game engine"
arch=('i686' 'x86_64' 'armv7h')
url="https://ihhub.github.io/fheroes2/"
license=('GPL-2.0-or-later')
depends=(
  hicolor-icon-theme
  sdl2_mixer
)
makedepends=(
  cmake
  gettext
  ninja
)
optdepends=(
  'curl: download demo version files (alternative to wget)'
  'innoextract: extract game resources from installer package'
  'python: extract animation resources from GOG CD image'
  'wget: download demo version files (alternative to curl)'
  'unzip: unpack demo version files'
)
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/ihhub/$pkgname/archive/$pkgver.tar.gz"
)
sha256sums=('e9a70f4cc831231010354cc599c84b626a18e15de1252bc35e4ced720857236c')

build() {
  cd "$pkgname-$pkgver"

  cmake -B build -G Ninja -S . \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/usr

  cmake --build build

  # build man page
  make -C docs
}

package() {
  cd "$pkgname-$pkgver"

  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 docs/fheroes2.6 "$pkgdir/usr/share/man/man6/fheroes2.6"
}

# vim:set ts=2 sw=2 et:
