# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=9.2.0
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc-fortran' 'python-setuptools' 'python-pip' 'autoconf' 'automake' 'libtool')
source=("$pkgname-$pkgver.tar.gz::https://github.com/code-saturne/code_saturne/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('f55cbf3209ac304732c2f07311a15ab4bcb803ab65e1aba918609706c7a9a44d29a5bcefb0e49521a8264661dbbc1c7a331dbcc1eb398c3192d5f8df0829ff2a')

build() {
	cd "$pkgname-$pkgver"
	./sbin/bootstrap
	./configure CC=cc CXX=g++ FC=gfortran --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
