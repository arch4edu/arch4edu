# Maintainer: Jed Brown <jed@59A2.org>
# Contributor: George Eleftheriou <eleftg>

pkgname=parmetis
pkgver=4.0.3.p6
_pkgver=4.0.3-p6
_pkgdirname=petsc-pkg-parmetis-475d8facbb32
_prefix=/usr
pkgrel=2
pkgdesc="A parallel graph partitioning library"
url="http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview"
arch=('i686' 'x86_64')
license=(custom)
depends=(openmpi metis)
makedepends=(cmake)
source=(https://bitbucket.org/petsc/pkg-parmetis/get/v${_pkgver}.tar.gz)
sha256sums=('663a20f45066d94a2732e8f38742047e89cd2b159cec7b3c6a7d834ae59d8b1f')

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
