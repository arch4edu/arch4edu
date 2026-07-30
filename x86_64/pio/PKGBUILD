# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

pkgname=pio
pkgver=2.7.0
pkgrel=1
pkgdesc="A high-level Parallel I/O Library for structured grid applications"
url="https://ncar.github.io/ParallelIO/"
license=('GPL')
depends=('netcdf-fortran-openmpi' 'gcc-fortran')
makedepends=('cmake' 'git')
optdepends=()
arch=('x86_64')
source=(https://github.com/NCAR/ParallelIO/archive/refs/tags/pio2_7_0.tar.gz)
sha256sums=('cce83743156ae723e7890931c2b48dcfe7ea8a276962dc4429f839d8f58d4a5a')

prepare() {
  cd ParallelIO-pio2_7_0
  # _FillValue macro removed from newer netcdf headers; use NC_FillValue instead
  sed -i 's/\b_FillValue\b/NC_FillValue/g' src/clib/pio_nc.c
}

build() {
  cd ParallelIO-pio2_7_0
  cmake -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_C_COMPILER=mpicc \
    -DCMAKE_Fortran_COMPILER=mpif90 \
    -DPIO_ENABLE_FORTRAN=ON \
    -DPIO_ENABLE_TIMING=OFF \
    -DPIO_ENABLE_DOC=OFF \
    -DPIO_ENABLE_EXAMPLES=OFF \
    -DWITH_PNETCDF=OFF \
    -DBUILD_SHARED_LIBS=ON
  cmake --build build
}

package() {
  cd ParallelIO-pio2_7_0
  DESTDIR="${pkgdir}" cmake --install build
}
