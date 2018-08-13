# Maintainer: Frank Siegert <frank.siegert@googlemail.com>
pkgname=fastjet
pkgver=3.3.1
pkgrel=2
pkgdesc="A particle physics package for jet finding in pp and e+e- collisions."
arch=('x86_64' 'i686')
url="http://fastjet.fr"
license=('GPL2')
groups=()
depends=(bash)
makedepends=(gcc-fortran python)
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=(http://fastjet.fr/repo/$pkgname-$pkgver.tar.gz)
noextract=()
md5sums=('4cc4e07abb1c2ccc54e040c346c3b433')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	./configure --prefix=/usr --enable-allplugins --enable-static=no --enable-pyext
	make
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	make -k check
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
