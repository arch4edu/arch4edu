# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: MatMoul <matmoul at the google email domain which is .com>
pkgname=octopi
pkgver=0.16.1
pkgrel=1
pkgdesc="A powerful Pacman frontend using Qt libs"
arch=('x86_64')
url="https://tintaescura.com/projects/octopi"
license=('GPL-2.0-or-later')
depends=(
  'alpm-octopi-utils'
  'qt-sudo'
  'qt6-5compat'
  'qtermwidget'
)
makedepends=(
  'cmake'
  'git'
  'qt6-tools'
)
optdepends=(
  'inxi: for SysInfo log'
  'lsb-release: for SysInfo log'
  'mhwd: for SysInfo log'
  'pacaur: for AUR support'
  'pacmanlogviewer: to view pacman log files'
  'paru: for AUR support'
  'pikaur: for AUR support'
  'systemd: for SysInfo log'
  'trizen: for AUR support'
  'yay: for AUR support'
)
provides=(
  'octopi-cachecleaner'
  'octopi-notifier'
  'octopi-repoeditor'
)
conflicts=(
  'octopi-notifier'
)
source=("$pkgname-$pkgver.tar.gz::https://github.com/aarnt/octopi/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('51908be24f04edb58c17570617082f8ff982ebf6670a8e618dc43ac063c25c80')

prepare() {
  cd "$pkgname-$pkgver"

  # Don't hardcode qt-sudo path
  sed -i 's/usr\/local/usr/g' src/constants.h
}

build() {
  cmake -B build -S "$pkgname-$pkgver" \
    -DCMAKE_BUILD_TYPE='None' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -Wno-dev
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  # remove duplicate license
  rm -r "$pkgdir/usr/share/licenses"
}
