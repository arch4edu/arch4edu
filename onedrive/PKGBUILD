# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Jameson Pugh <imntreal@gmail.com>

pkgname=onedrive
pkgver=1.1.4
pkgrel=1
pkgdesc='Free OneDrive client written in D'
arch=('i686' 'x86_64')
url='https://github.com/skilion/onedrive'
license=('GPL3')
depends=('curl' 'gcc-libs' 'glibc' 'sqlite')
makedepends=('dmd')
source=("$pkgname-$pkgver.tar.gz::https://github.com/skilion/onedrive/archive/v$pkgver.tar.gz")
sha256sums=('c6ef18c5798ce70c32843f2bed73600af5ad342fd20239c973887e9e751a35b6')

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
