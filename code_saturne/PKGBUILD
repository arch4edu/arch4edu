# Maintainer: Vlad V. Voronenkov <vladvoronenkov at yandex dot ru>
# Contribuor: Jingbei Li
# Contributor: Heavysink <winstonwu91@gmail.com>
pkgname=code_saturne
pkgver=6.0.4
pkgrel=1
pkgdesc="An open source CFD software which solves the Navier-Stokes equations under different circumstances."
arch=(x86_64)
url="http://code-saturne.org"
license=('GPL')
depends=('libxml2' 'python-pyqt5' 'cgns' 'parmetis' 'scotch' 'med' 'hdf5')
makedepends=('doxygen' 'graphviz' 'gcc8-fortran')
source=("http://code-saturne.org/cms/sites/default/files/releases/$pkgname-$pkgver.tar.gz")
sha512sums=('a2bfd1209e77a2770532641e5b78fd4ce27013e382dc24394f6fe9b74ed1ea4bf80c6b4d0ab648fc4c8ba3ed7ecca0242ef3d023a19d4e8a5b928bbd7f1f96e9')

build() {
	cd "$pkgname-$pkgver"
	./configure CC=cc-8 CXX=g++-8 FC=gfortran-8 --enable-shared --with-metis=/usr --with-scotch=/usr --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
