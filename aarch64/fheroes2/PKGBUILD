pkgname=fheroes2
pkgver=1.1.17
pkgrel=1
pkgdesc="Recreation of the Heroes of Might and Magic II game engine"
arch=('i686' 'x86_64' 'armv7h')
url="https://ihhub.github.io/fheroes2/"
license=('GPL-2.0-or-later')
depends=(
  glibc
  hicolor-icon-theme
  libgcc
  libstdc++
  sdl2
  sdl2_mixer
  zlib
)
makedepends=(
  cmake
  gettext
  ninja
)
optdepends=(
  'bash: download demo and extract game resources'
  'curl: download demo version files (alternative to wget)'
  'innoextract: extract game resources from installer package'
  'python: extract animation resources from GOG CD image'
  'wget: download demo version files (alternative to curl)'
  'unzip: unpack demo version files'
)
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/ihhub/$pkgname/archive/$pkgver.tar.gz"
)
sha256sums=('29f0be1a15ecce658e647b8c3d3fe2e6acddf6fa2144b1e05c82984846f568a1')

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
