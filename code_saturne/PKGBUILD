# Maintainer: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=6.0.0
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('openmpi' 'libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5-openmpi')
makedepends=('doxygen' 'graphviz' 'gcc-fortran' 'hdf5-openmpi')
source=("http://code-saturne.org/cms/sites/default/files/releases/$pkgname-$pkgver.tar.gz")
md5sums=('be9ea1760896b8f681e5995a11f7129f')

build() {
	cd "$pkgname-$pkgver"
	CC=mpicc CXX=mpicxx FC=mpif90 ./configure --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
