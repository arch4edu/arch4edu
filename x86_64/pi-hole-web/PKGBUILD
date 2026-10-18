# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>

pkgname=pi-hole-web
_mainpkgname=pi-hole
_pkgname=web
pkgver=6.6.1
pkgrel=1
pkgdesc='Pi-hole Dashboard for stats and more.'
arch=('any')
license=('EUPL-1.2')
url="https://github.com/pi-hole/web"
depends=()
makedepends=()
conflicts=()
install=$pkgname.install
backup=()

source=($_pkgname-$pkgver.tar.gz::https://github.com/$_mainpkgname/$_pkgname/archive/refs/tags/v$pkgver.tar.gz)
sha256sums=('34d82b58a0b601803769e66c0f3e1d8bd06513449625e38e07afa007399284d9')

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
