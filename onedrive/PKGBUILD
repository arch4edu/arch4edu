# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Jameson Pugh <imntreal@gmail.com>

pkgname=onedrive
pkgver=1.1.3
pkgrel=1
pkgdesc='Free OneDrive client written in D'
arch=('i686' 'x86_64')
url='https://github.com/skilion/onedrive'
license=('GPL3')
depends=('curl' 'gcc-libs' 'glibc' 'sqlite')
makedepends=('dmd')
source=("$pkgname-$pkgver.tar.gz::https://github.com/skilion/onedrive/archive/v$pkgver.tar.gz")
sha256sums=('fb12235a73919b3374b8f27785b834a690fba1c6e70c6e6f1f5da3e51eb471a0')

prepare() {
  printf 'v%s\n' "$pkgver" > $pkgname-$pkgver/version
  sed -i '/^onedrive:/ s/version //' $pkgname-$pkgver/Makefile
}

build() {
  make PREFIX=/usr -C $pkgname-$pkgver
}

package() {
  make PREFIX=/usr DESTDIR="$pkgdir" -C $pkgname-$pkgver install
  install -Dm644 $pkgname-$pkgver/config "$pkgdir/usr/share/onedrive/config.default"
}
