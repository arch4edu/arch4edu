# -*- shell-script -*-
# Maintainer: Ivan Shapovalov <intelfx@intelfx.name>
# Contributor: goodmen <goodmenzy@gmail.com>

pkgname=crosstool-ng-git
epoch=1
pkgver=1.22.0.r148.g7300eb1
pkgrel=1
pkgdesc="crosstool-NG aims at building toolchains."
arch=('i686' 'x86_64')
url="http://crosstool-ng.org/"
license=('GPL')
depends=('ncurses' 'make')
makedepends=('git' 'flex' 'bison' 'gperf' 'help2man')
provides=('crosstool-ng')
conflicts=('crosstool-ng')
source=('git://github.com/crosstool-ng/crosstool-ng')
md5sums=('SKIP')

pkgver() {
	cd crosstool-ng

	git describe --long --tags | sed 's/^crosstool-ng-//;s/-/.r/;s/-/./'
}

build () {
	cd crosstool-ng

	./bootstrap
	./configure --prefix=/usr
	make
}

package () {
	cd crosstool-ng

	make DESTDIR="$pkgdir" install
	install -Dm644 ct-ng.comp "$pkgdir/etc/bash_completion.d/ct-ng"
}
