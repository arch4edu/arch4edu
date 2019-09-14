pkgname=pio
pkgver=2.4.4
pkgrel=1
pkgdesc="A high-level Parallel I/O Library for structured grid applications"
url="https://ncar.github.io/ParallelIO/"
license=('GPL')
depends=('netcdf-fortran-openmpi' 'gcc-fortran')
optdepends=()
arch=('x86_64')
source=(https://github.com/NCAR/ParallelIO/releases/download/${pkgname}${pkgver//./_}/${pkgname}-${pkgver}.tar.gz)
sha256sums=('69ed1535b16b3b5a42b37849e324cf9d2f4fa5d9fa87092e3574642eb12355e9')

build() {
  cd ${pkgname}-${pkgver}
  CC=mpicc FC=mpif90 ./configure --prefix=/usr --enable-fortran
  make
}

check() {
    cd "$pkgname-$pkgver"
    make check
}

package() {
  cd ${pkgbase}-${pkgver}
  make DESTDIR=${pkgdir} install
}
