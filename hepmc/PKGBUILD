# Maintainer: Frank Siegert <frank.siegert@googlemail.com>
pkgname=hepmc
pkgver=2.06.09
pkgrel=2
pkgdesc="A particle physics package for storing collision events from Monte Carlo generators."
arch=('x86_64' 'i686')
url="http://lcgapp.cern.ch/project/simu/HepMC/"
license=('GPL2')
groups=()
depends=(bash)
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=(http://lcgapp.cern.ch/project/simu/HepMC/download/HepMC-$pkgver.tar.gz)
noextract=()
md5sums=('c47627ced4255b40e731b8666848b087')

build() {
	cd "$srcdir/HepMC-$pkgver"
	./configure --prefix=/usr --with-momentum=GEV --with-length=MM
	make
}

package() {
	cd "$srcdir/HepMC-$pkgver"
	make DESTDIR="$pkgdir/" install
}
