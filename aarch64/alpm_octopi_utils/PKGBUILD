# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: MatMoul <matmoul at the google email domain which is .com>
pkgname=alpm_octopi_utils
pkgver=1.0.2
pkgrel=5
pkgdesc="Alpm utils for Octopi"
arch=('x86_64')
url="https://github.com/aarnt/alpm_octopi_utils"
license=('GPL-3.0-or-later')
depends=('pacman-contrib')
makedepends=('git' 'vala')
provides=('alpm-octopi-utils')
_commit=1e735c3a27803ca5b6470e946f9cac708143dfd9  # master
source=("git+https://github.com/aarnt/alpm_octopi_utils.git#commit=$_commit"
        'https://github.com/aarnt/alpm_octopi_utils/pull/4.patch')
sha256sums=('SKIP'
            'c117f3a86f6428f671723b921229fdfe3e61b057efae1e0b3b2b1a2993ef8842')

prepare() {
  cd alpm_octopi_utils

  # Add DESTDIR to Makefile
  patch -Np1 -i ../4.patch
}

build() {
  cd alpm_octopi_utils
  make
}

package() {
  cd alpm_octopi_utils
  make DESTDIR="$pkgdir" install
}
