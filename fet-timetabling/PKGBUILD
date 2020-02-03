# Maintainer: Thibaud Kehler <thibaud.kehler at gmx dot net>
pkgname='fet-timetabling'
_module='fet'
pkgver=5.39.0
pkgrel=1
pkgdesc="A software for automatically scheduling the timetable of a school, high-school or university."
arch=('x86_64' 'i686')
url="http://lalescu.ro/liviu/fet/"
license=('AGPL3')
depends=('qt5-base' 'hicolor-icon-theme')
source=("http://lalescu.ro/liviu/fet/download/$_module-$pkgver.tar.bz2")
md5sums=('243a0d63d312a91e4d23fef3fdc02003')

build() {
	cd "$srcdir/$_module-$pkgver"
	qmake-qt5 fet.pro "DEFINES+=USE_SYSTEM_LOCALE"
	make
}

package() {
	cd "$srcdir/$_module-$pkgver"
	make INSTALL_ROOT="${pkgdir}/" install
}
