# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=8.1.1
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc-fortran')
source=("http://code-saturne.org/releases/$pkgname-$pkgver.tar.gz")
sha512sums=('33f2f4873f2998b624c310425ce0c0a3e76ced30b924106217cec83c2482a176c1eb91264ca0d99e4b4685f527836883f1d882a281bb2063fad00327c7b33f1b')

build() {
	cd "$pkgname-$pkgver"
	./configure CC=cc CXX=g++ FC=gfortran --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
