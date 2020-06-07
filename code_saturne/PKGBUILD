# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=6.0.2
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc8-fortran')
source=("http://code-saturne.org/cms/sites/default/files/releases/$pkgname-$pkgver.tar.gz")
sha512sums=('2b66b063dcdbbfc049336b570d2484adf424441d8b2ca51c9bc636512f57b1ab9a4d8ed21cfe2a115b38c64c8159a3f1f4e4c5cca9d4808e24c62a7a21e40974')

build() {
	cd "$pkgname-$pkgver"
	./configure CC=cc-8 CXX=g++-8 FC=gfortran-8 --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
