pkgname=pio
pkgver=2.5.2
pkgrel=2
pkgdesc="A high-level Parallel I/O Library for structured grid applications"
url="https://ncar.github.io/ParallelIO/"
license=('GPL')
depends=('netcdf-fortran-openmpi' 'gcc-fortran')
optdepends=()
arch=('x86_64')
source=(https://github.com/NCAR/ParallelIO/releases/download/${pkgname}${pkgver//./_}/${pkgname}-${pkgver}.tar.gz)
sha256sums=('378e6d01dbfb9e99a913be814d3a4f04f93a3bb9f860468ccaf199ed3687acac')

build() {
  cd ${pkgname}-${pkgver}
  CC=mpicc FC=mpif90 ./configure --prefix=/usr --enable-fortran
  make
}

#check() {
#    cd "$pkgname-$pkgver"
#    make check
#}

package() {
  cd ${pkgbase}-${pkgver}
  make DESTDIR=${pkgdir} install
}
