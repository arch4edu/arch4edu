# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Gianluca Pettinello <g_pet@hotmail.com>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=13.4.1
_pkgver=${pkgver//./-}
pkgrel=1
pkgdesc="algorithms for the solution of large-scale scientific problems"
arch=('x86_64')
url="http://trilinos.org"
license=('LGPL3')
depends=('python' 'lapack' 'boost' 'netcdf' 'libmatio' 'libx11' 'hdf5-openmpi')
makedepends=('gcc-fortran' 'perl' 'blas' 'cmake' 'bc' 'python-numpy')
checkdepends=('cmake')
source=("https://github.com/trilinos/Trilinos/archive/refs/tags/trilinos-release-$_pkgver.tar.gz"
        'compiler-errors.patch')
sha256sums=('5465cbff3de7ef4ac7d40eeff9d99342c00d9d20eee0a5f64f0a523093f5f1b3'
            'a255f689d3a65187635a7dea2862b7c323c6efbc65501069bfe0cea7669d12a3')

prepare() {
  patch -d  Trilinos-trilinos-release-"$_pkgver" -p1 -i ../compiler-errors.patch
}

build() {
    cd Trilinos-trilinos-release-"$_pkgver"
    mkdir -p build
    cd build

    cmake .. -DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
             -DTrilinos_ENABLE_ALL_PACKAGES:BOOL=ON \
             -DTrilinos_ENABLE_PyTrilinos:BOOL=OFF \
             -DTrilinos_ENABLE_Gtest:BOOL=OFF \
             -DTrilinos_ENABLE_TESTS=OFF \
             -DTPL_ENABLE_gtest:BOOL=OFF \
             -DTPL_ENABLE_MPI:BOOL=ON \
             -DTPL_ENABLE_HDF5:BOOL=ON \
             -DCMAKE_INSTALL_PREFIX:PATH=/usr \
             -DBUILD_SHARED_LIBS:BOOL=ON \
             -DCMAKE_Fortran_FLAGS=-fallow-argument-mismatch
    make VERBOSE=1
}

check() {
    cd Trilinos-trilinos-release-"$_pkgver"/build
    ctest
}

package() {
    cd Trilinos-trilinos-release-"$_pkgver"/build
    make DESTDIR="$pkgdir" install
}
