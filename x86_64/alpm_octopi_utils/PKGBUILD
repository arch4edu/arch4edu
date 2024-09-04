# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: MatMoul <matmoul at the google email domain which is .com>
pkgname=alpm_octopi_utils
pkgver=1.0.2
pkgrel=7
pkgdesc="Alpm utils for Octopi"
arch=('x86_64')
url="https://github.com/aarnt/alpm_octopi_utils"
license=('GPL-3.0-or-later')
depends=('pacman-contrib')
makedepends=('cmake' 'git' 'vala')
provides=('alpm-octopi-utils')
_commit=1e735c3a27803ca5b6470e946f9cac708143dfd9  # master
source=("git+https://github.com/aarnt/alpm_octopi_utils.git#commit=${_commit}")
sha256sums=('006ba126ed4ed99de6f3be8fba152cdeebd1048724d902d7e98f1a9eb98d4ca4')

build() {
  cmake -B build -S alpm_octopi_utils \
    -DCMAKE_BUILD_TYPE='None' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -Wno-dev
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
