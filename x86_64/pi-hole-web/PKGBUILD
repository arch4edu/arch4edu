# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>

pkgname=pi-hole-web
_mainpkgname=pi-hole
_pkgname=web
pkgver=6.5.1
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
sha256sums=('db0603d1f1a3679cc2ee5b30bb738c178666c4230dd1a9b49917ed56ef9aa7e9')

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
