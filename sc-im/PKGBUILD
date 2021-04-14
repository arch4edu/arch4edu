# Maintainer: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>
# Contributor: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>

pkgname=sc-im
pkgver=0.8.1
pkgrel=1
pkgdesc='A spreadsheet program based on SC'
arch=('i686' 'x86_64' 'armv7h')
url='https://github.com/andmarti1424/sc-im'
depends=(libxml2 libzip)
optdepends=('libxlsxwriter: export to xlsx. Requires rebuild of sc-im'
            'gnuplot: create graphs')
license=('BSD')
conflicts=('scim-spreadsheet' 'sc-im-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/andmarti1424/$pkgname/archive/v${pkgver}.tar.gz"
        'arch.0.8.0.patch')
sha256sums=('73958f2adf2548be138f90a1fa2cb3a9c316a6d8d78234ebb1dc408cbf83bac7'
            '191c8537f75decb0bf8d00db9543b07985684bf10308ff63c6648de70b7ff6e5')
MAKEFLAGS='-j1'

prepare() {
  cd "$pkgname-$pkgver/src"
  # install things in the correct place for package managers
  patch <"$srcdir/arch.0.8.0.patch"
}

build() {
  cd "$pkgname-$pkgver/src"
  make CC='gcc -fcommon'
}

package() {
  cd "$pkgname-$pkgver/src"
  make DESTDIR="$pkgdir" install

  install -D -m644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
