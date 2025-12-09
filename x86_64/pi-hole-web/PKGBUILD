# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>

pkgname=pi-hole-web
_mainpkgname=pi-hole
_pkgname=web
pkgver=6.4
pkgrel=1
pkgdesc='Pi-hole Dashboard for stats and more.'
arch=('any')
license=('EUPL-1.2')
url="https://github.com/pi-hole/pi-hole"
depends=()
makedepends=()
conflicts=()
install=$pkgname.install
backup=()

source=($_pkgname-$pkgver.tar.gz::https://github.com/$_mainpkgname/$_pkgname/archive/refs/tags/v$pkgver.tar.gz
        "https://raw.githubusercontent.com/max72bra/pi-hole-web-customization/main/arch-web-$pkgver-$pkgrel.patch"
)

sha256sums=('4501ccbd3a2c429644e10dae68bf3738ab715031ed29607e2d17e80e8a569d03'
            'bf90cbf556772f2debf6e2d65d9a01408795d069ec77ca57aeca7c8908824e1d')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  patch -Np1 -i "$srcdir"/arch-web-$pkgver-$pkgrel.patch
}

package() {
  cd "$srcdir"

  install -dm755 "$pkgdir"/var/www/html/admin

  cp -dpr --no-preserve=ownership $_pkgname-$pkgver/* "$pkgdir"/var/www/html/admin

  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 $_pkgname-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/AdminLTE

  rm "$pkgdir"/var/www/html/admin/*.md
  rm "$pkgdir"/var/www/html/admin/LICENSE
  rm "$pkgdir"/var/www/html/admin/package*.json
}
