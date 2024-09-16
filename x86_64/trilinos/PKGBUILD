# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Gianluca Pettinello <g_pet@hotmail.com>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=16.0.0
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
sha512sums=('ed8b9f6ec8d35879f28f066685f70c492ee83ffdc42cfed75750216c0c689c81b00355520a7db441e56d83a6a153b0dbe4f8422d163a942cdcc6786235f64688')


build() {
  cmake -S Trilinos-trilinos-release-"$_pkgver" \
        -B build \
        -D CMAKE_INSTALL_PREFIX:PATH=/usr \
        -D BUILD_SHARED_LIBS:BOOL=ON \
        -D Trilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
        -D Trilinos_ENABLE_ALL_PACKAGES:BOOL=ON \
        -D Trilinos_ENABLE_SECONDARY_TESTED_CODE:BOOL=ON \
        -D Trilinos_ENABLE_PyTrilinos:BOOL=OFF \
        -D Trilinos_ENABLE_Gtest:BOOL=OFF \
        -D Trilinos_ENABLE_TESTS:BOOL=OFF \
        -D Trilinos_ENABLE_TrilinosFrameworkTests:BOOL=OFF \
        -D Trilinos_ENABLE_TrilinosATDMConfigTests:BOOL=OFF \
        -D TPL_ENABLE_gtest:BOOL=OFF \
        -D TPL_ENABLE_MPI:BOOL=ON \
        -D TPL_ENABLE_HDF5:BOOL=ON \
        -D Zoltan_ENABLE_F90INTERFACE:BOOL=ON \
        -D CMAKE_C_FLAGS="$CFLAGS -Wno-incompatible-pointer-types" \
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
