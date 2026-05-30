# Maintainer: harrietobrien <harrietobrien@protonmail.com>
# Contributor: Ed Sandberg <scarypezsanta@gmail.com>
# Contributor: Xyne

pkgname=abinit
pkgver=10.6.7
pkgrel=1
pkgdesc="Full-featured atomic-scale first-principles simulation software."
arch=('i686' 'x86_64')
url="https://www.abinit.org/"
license=('GPLv3')
depends=('lapack' 'blas' 'openmpi' 'netcdf' 'netcdf-fortran' 'hdf5' 'libxc')
makedepends=('gcc-fortran' 'perl')
source=("https://github.com/${pkgname}/${pkgname}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('705199f8c09f975df1f7db0c499ece452af96148d131f41dc45dfbd1cfa4190c')

prepare() {
  export FCFLAGS="-w -fallow-argument-mismatch -O2"
  export FFLAGS="-w -fallow-argument-mismatch -O2"
}

build() {
  cd -- "$srcdir/$pkgname-$pkgver"
  ./config/scripts/makemake
  mkdir -p build && cd build
  ../configure \
    FC="mpifort" \
    CC="mpicc"
  make
}

package() {
  cd -- "$srcdir/$pkgname-$pkgver/build"
  make DESTDIR="$pkgdir" install
}
