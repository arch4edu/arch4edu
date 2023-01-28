# Maintainer: Jed Brown <jed@59A2.org>
# Contributor: George Eleftheriou <eleftg>

pkgname=parmetis
pkgver=4.0.3.p9
_pkgver=4.0.3-p9
_pkgdirname=petsc-pkg-parmetis-f5e3aab04fd5
_prefix=/usr
pkgrel=1
pkgdesc="A parallel graph partitioning library"
url="http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview"
arch=('i686' 'x86_64')
license=(custom)
depends=(openmpi metis)
makedepends=(cmake)
source=(https://bitbucket.org/petsc/pkg-parmetis/get/v${_pkgver}.tar.gz)
sha256sums=('612717e85992c984f09b0f5670be421bbb90a4c04145ab5b9a3358b92765d891')

# "Upstream" is unmaintained and does not reply or apply to critical patches
#source=(http://glaros.dtc.umn.edu/gkhome/fetch/sw/parmetis/parmetis-$pkgver.tar.gz)

build() {
  cd "$srcdir/${_pkgdirname}"
  make config cc=${_prefix}/bin/mpicc mpicc=${_prefix}/bin/mpicc mpicxx=${_prefix}/bin/mpicxx shared=1 prefix=${_prefix}
  make
}

package () {
  cd "$srcdir/${_pkgdirname}"
  make install "DESTDIR=$pkgdir"
}
