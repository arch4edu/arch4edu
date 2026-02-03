# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=9.1.0
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc-fortran' 'python-setuptools' 'python-pip')
source=("http://code-saturne.org/releases/$pkgname-$pkgver.tar.gz")
sha512sums=('f92c3ea1a44943376b29e3453dec95ca3497bf4d546f66f9c2dbe8fc72f0b6043f2e69a9af299cf2f185d665fe21c2ba74576538a53b2f36fce9fa4cb5ad4ba8')

build() {
	cd "$pkgname-$pkgver"
	./configure CC=cc CXX=g++ FC=gfortran --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
