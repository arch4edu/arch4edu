# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=7.0.2
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc-fortran')
source=("http://code-saturne.org/cms/sites/default/files/releases/$pkgname-$pkgver.tar.gz")
sha512sums=('183ec51cf7bdce2449fbb595dbbc833328b8268f43a2f904eb4d215d9758b18c55e53c878211b017522c0ea5c0e476e4db9fd339ef5a80d3e10a2a4e3b5b9eaa')

build() {
	cd "$pkgname-$pkgver"
	./configure CC=cc CXX=g++ FC=gfortran --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
