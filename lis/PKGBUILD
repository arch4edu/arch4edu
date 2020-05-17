# Maintainer: Heavysink <winstonwu91 at gmail>
pkgname=lis
pkgver=2.0.21
pkgrel=1
pkgdesc="Library of Iterative Solvers for linear systems"
arch=(i686 x86_64)
url="http://www.ssisc.org/lis"
license=('GPL3')
depends=('openmpi')
makedepends=('git' 'gcc-fortran')
source=("git://github.com/anishida/lis.git#branch=master")
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$pkgname"
    git describe --tags $(git rev-list --tags --max-count=1)
}

build() {
  cd "$srcdir/$pkgname"
    export FFLAGS+=" -fallow-argument-mismatch"
    export FCFLAGS+=" -fallow-argument-mismatch"

  ./configure \
    --prefix=/usr \
    --enable-mpi \
    --enable-omp \
    --enable-shared \
    --enable-fma \
    --enable-sse2 \
    --enable-longlong \
    --enable-longdouble \
    --enable-quad \
    --enable-f90 \
    --enable-fortran
  make
}

check() {
  cd "$srcdir/$pkgname"
  make check
 }
 
package()
{
  cd "$srcdir/$pkgname"
  make install DESTDIR=$pkgdir
}
