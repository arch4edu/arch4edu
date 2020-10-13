# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=6.0.5
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc8-fortran')
source=("http://code-saturne.org/cms/sites/default/files/releases/$pkgname-$pkgver.tar.gz")
sha512sums=('7b3b20cdbce8bfec6ce0125ff30852721b0ee5a6e841329e1ab91f31a439012d7e7c2221badd9a7788980d461f365722d80e1b7540304d434b50527531531765')

build() {
	cd "$pkgname-$pkgver"
	./configure CC=cc-8 CXX=g++-8 FC=gfortran-8 --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
