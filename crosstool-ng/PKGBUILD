# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: jwwolf <jwwolf+arch@gmail.com>
# Contributor: Bernhard Walle <bernhard@bwalle.de>

pkgname=crosstool-ng
pkgver=1.22.0
pkgrel=1
pkgdesc='Versatile (cross-)toolchain generator'
arch=('i686' 'x86_64')
url='http://crosstool-ng.org/'
license=('GPL')
depends=('make' 'gperf' 'wget')
makedepends=('help2man')
options=('!makeflags')
source=(http://crosstool-ng.org/download/$pkgname/$pkgname-$pkgver.tar.bz2)
md5sums=('23d5de6b95f86ad2674bcf6859b9664f')
sha256sums=('d6338a9b33f9d972167049bbe76e88b1e9248466a53df08dcfe8bcfe849d8d83')

build() {
  cd $pkgname
  ./configure --prefix=/usr
  make
}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" install
  install -Dm644 ct-ng.comp "$pkgdir"/usr/share/bash-completion/completions/ct-ng
}
