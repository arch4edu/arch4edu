# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Gianluca Pettinello <g_pet@hotmail.com>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=15.1.1
_pkgver=${pkgver//./-}
pkgrel=1
pkgdesc="algorithms for the solution of large-scale scientific problems"
arch=('x86_64')
url="http://trilinos.org"
license=('LGPL3')
depends=('python' 'lapack' 'boost' 'netcdf-openmpi' 'libmatio' 'libx11' 'hdf5-openmpi')
makedepends=('gcc-fortran' 'perl' 'blas' 'cmake' 'bc' 'python-numpy')
provides=('trilinos-sacado' 'trilinos-ml' 'zoltan' 'kokkos')
checkdepends=('cmake')
source=("https://github.com/trilinos/Trilinos/archive/refs/tags/trilinos-release-$_pkgver.tar.gz")
sha512sums=('5a1a7d321dd3b47fafe0422884d1a7bf6731d5ee806a4fd1bf31f179ca5d6f4290cda4515d0d7786024ea15c17e88422a9518370c5cfb32b4b44761de232e0de')


build() {
  cmake -S Trilinos-trilinos-release-"$_pkgver" \
        -B build \
        -D CMAKE_INSTALL_PREFIX:PATH=/usr \
        -D BUILD_SHARED_LIBS:BOOL=ON \
        -D Trilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
        -D Trilinos_ENABLE_ALL_PACKAGES:BOOL=ON \
        -D Trilinos_ENABLE_PyTrilinos:BOOL=OFF \
        -D Trilinos_ENABLE_Gtest:BOOL=OFF \
        -D Trilinos_ENABLE_TESTS:BOOL=OFF \
        -D Trilinos_ENABLE_TrilinosFrameworkTests:BOOL=OFF \
        -D Trilinos_ENABLE_TrilinosATDMConfigTests:BOOL=OFF \
        -D TPL_ENABLE_gtest:BOOL=OFF \
        -D TPL_ENABLE_MPI:BOOL=ON \
        -D TPL_ENABLE_HDF5:BOOL=ON \
        -D CMAKE_Fortran_FLAGS="$FCFLAGS -fallow-argument-mismatch"
  make -C build
}

check() {
  cd build
  ctest
}

package() {
  DESTDIR=${pkgdir} cmake --install build
}
