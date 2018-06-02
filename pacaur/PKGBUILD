pkgname=pacaur
pkgver=4.7.90
pkgrel=1
pkgdesc="An AUR helper that minimizes user interaction"
arch=('any')
url="https://github.com/rmarquis/pacaur"
license=('ISC')
depends=('cower' 'expac' 'sudo' 'git')
makedepends=('perl')
backup=('etc/xdg/pacaur/config')
source=("$pkgname-$pkgver.tar.gz::https://github.com/rmarquis/$pkgname/archive/$pkgver.tar.gz")
md5sums=('237a716ddfe3eab43a0f7958be646d09')

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    make install DESTDIR=$pkgdir PREFIX=/usr
}

