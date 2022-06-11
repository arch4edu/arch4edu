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
source=("$pkgname-$pkgver.tar.gz::https://github.com/skilion/onedrive/archive/v$pkgver.tar.gz"
        'https://github.com/skilion/onedrive/commit/8001e1c025ddd6c2532b03305c59e407457d059b.patch')
sha256sums=('c6ef18c5798ce70c32843f2bed73600af5ad342fd20239c973887e9e751a35b6'
            '9c744314c920a73a5997fa861187b097964e47cb44ce47ff45ffebff8346fc8b')

prepare() {
  cd $pkgname-$pkgver

  printf 'v%s\n' "$pkgver" > version
  sed -i '/^onedrive:/ s/version //' Makefile
  patch -Np 1 < ../8001e1c025ddd6c2532b03305c59e407457d059b.patch
}

build() {
  make PREFIX=/usr -C $pkgname-$pkgver
}

package() {
  make PREFIX=/usr DESTDIR="$pkgdir" -C $pkgname-$pkgver install
  install -Dm644 $pkgname-$pkgver/config "$pkgdir/usr/share/onedrive/config.default"
}
