# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Gianluca Pettinello <g_pet@hotmail.com>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=14.0.0
_pkgver=${pkgver//./-}
pkgrel=1
pkgdesc="algorithms for the solution of large-scale scientific problems"
arch=('x86_64')
url="http://trilinos.org"
license=('LGPL3')
depends=('python' 'lapack' 'boost' 'netcdf' 'libmatio' 'libx11' 'hdf5-openmpi')
makedepends=('gcc-fortran' 'perl' 'blas' 'cmake' 'bc' 'python-numpy')
provides=('trilinos-sacado' 'zoltan')
checkdepends=('cmake')
source=("https://github.com/trilinos/Trilinos/archive/refs/tags/trilinos-release-$_pkgver.tar.gz"
        'compiler-errors.patch')
sha256sums=('054d2fabdf70fce0dfaeb20eed265bd7894045d3e00c3d1ddb72d1c77c339ca1'
            '09546864a36ec83cfbedb29c97ead05778b4da370a84185565973f28f49f2880')

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
             -DTrilinos_ENABLE_TESTS:BOOL=OFF \
             -DTrilinos_ENABLE_TrilinosFrameworkTests:BOOL=OFF \
             -DTrilinos_ENABLE_TrilinosATDMConfigTests:BOOL=OFF \
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
