# Maintainer: Thibaud Kehler <thibaud.kehler at gmx dot net>
pkgname='fet-timetabling'
_module='fet'
pkgver=5.44.0
pkgrel=1
pkgdesc="A software for automatically scheduling the timetable of a school, high-school or university."
arch=('x86_64' 'i686')
url="http://lalescu.ro/liviu/fet/"
license=('AGPL3')
depends=('qt5-base' 'hicolor-icon-theme')
source=("http://lalescu.ro/liviu/fet/download/$_module-$pkgver.tar.bz2")
md5sums=('d511f430034cac86be9d7e8c9bc8202d')

build() {
	cd "$srcdir/$_module-$pkgver"
	qmake-qt5 fet.pro "DEFINES+=USE_SYSTEM_LOCALE"
	make
}

package() {
	cd "$srcdir/$_module-$pkgver"
	make INSTALL_ROOT="${pkgdir}/" install
}
