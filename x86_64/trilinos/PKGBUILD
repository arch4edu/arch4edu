# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Gianluca Pettinello <g_pet@hotmail.com>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=16.1.0
_pkgver=${pkgver//./-}
pkgrel=2
pkgdesc="algorithms for the solution of large-scale scientific problems"
arch=('x86_64')
url="http://trilinos.org"
license=('LGPL3')
depends=('python' 'lapack' 'boost' 'netcdf-openmpi' 'libmatio' 'libx11' 'hdf5-openmpi')
makedepends=('gcc-fortran' 'perl' 'blas' 'cmake' 'bc' 'python-numpy')
provides=('trilinos-sacado' 'trilinos-ml' 'zoltan' 'kokkos')
checkdepends=('cmake')
source=("https://github.com/trilinos/Trilinos/archive/refs/tags/trilinos-release-$_pkgver.tar.gz")
sha512sums=('8a8e565e6ecbfc6a16c3a2e071bd7a0c89b0b31a02fe0acc51734c90de1fbdce9758b129b0455ddaa131654f7ea643d87d96ae2fe22bf3f35b332415a3a62c14')

prepare() {
  cd Trilinos-trilinos-release-"$_pkgver"/packages/pliris/src
  sed -i -e 's/double seconds()/double seconds(double)/g' xlu_solve_new.c
  sed -i -e 's/double seconds()/double seconds(double)/g' x_factor.c
}

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
        -D HDF5_LIBRARY_NAMES:STRING='hdf5;hdf5_hl;hdf5_tools' \
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
