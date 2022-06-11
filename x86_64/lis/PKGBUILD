# Maintainer: Heavysink <winstonwu91 at gmail>
pkgname=lis
pkgver=2.0.30
pkgrel=1
pkgdesc="Library of Iterative Solvers for linear systems"
arch=(i686 x86_64)
url="http://www.ssisc.org/lis"
license=('GPL3')
depends=('openmpi')
makedepends=('gcc-fortran')
source=("https://github.com/anishida/lis/archive/${pkgver}.tar.gz")
md5sums=('f600359131fc669a49adfc6516fa1fc0')

build() {
  cd "$srcdir/$pkgname-$pkgver"
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
  cd "$srcdir/$pkgname-$pkgver"
  make check
 }
 
package()
{
  cd "$srcdir/$pkgname-$pkgver"
  make install DESTDIR=$pkgdir
}
