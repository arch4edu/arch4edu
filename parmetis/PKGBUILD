# Maintainer: Jed Brown <jed@59A2.org>
# Contributor: George Eleftheriou <eleftg>

pkgname=parmetis
pkgver=4.0.3.p2
_pkgver=4.0.3-p2
_prefix=/usr
pkgrel=1
pkgdesc="A parallel graph partitioning library"
url="http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview"
arch=('i686' 'x86_64')
license=(custom)
depends=(metis openmpi)
makedepends=(cmake)
source=(http://ftp.mcs.anl.gov/pub/petsc/externalpackages/parmetis-${_pkgver}.tar.gz)
sha256sums=('3b55b2932f694b4270fab0f65e5ae36f93ca9e899b06bf9825a647653787bcd5')
# "Upstream" is unmaintained and does not reply or apply to critical patches
#source=(http://glaros.dtc.umn.edu/gkhome/fetch/sw/parmetis/parmetis-$pkgver.tar.gz)

build() {
  cd "$srcdir/parmetis-${_pkgver}"
  make config cc=${_prefix}/bin/mpicc mpicc=${_prefix}/bin/mpicc mpicxx=${_prefix}/bin/mpicxx shared=1 prefix=${_prefix}
  make
}

package () {
  cd "$srcdir/parmetis-${_pkgver}"
  make install "DESTDIR=$pkgdir"
}
