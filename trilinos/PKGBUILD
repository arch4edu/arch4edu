# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=13.0.1
_pkgver=${pkgver//./-}
pkgrel=2
pkgdesc="algorithms for the solution of large-scale scientific problems"
arch=('x86_64')
url="http://trilinos.org"
license=('LGPL3')
depends=('python' 'lapack' 'boost' 'netcdf' 'libmatio' 'libx11' 'hdf5-openmpi')
makedepends=('gcc-fortran' 'perl' 'blas' 'cmake' 'doxygen' 'bc' 'python-numpy' 'swig')
checkdepends=('cmake')
source=("https://github.com/trilinos/Trilinos/archive/trilinos-release-$_pkgver.tar.gz"
        'python-mpi-version.patch')
sha256sums=('0bce7066c27e83085bc189bf524e535e5225636c9ee4b16291a38849d6c2216d'
            '9920ddf718ff04a14d1263623dfd98791404b1db0a73d95ba48d87215e8409eb')

prepare() {
  patch -d  Trilinos-trilinos-release-"$_pkgver" -p1 -i ../python-mpi-version.patch
}

build() {
    cd Trilinos-trilinos-release-"$_pkgver"
    mkdir -p build
    cd build

    cmake .. -DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
             -DTrilinos_ENABLE_ALL_PACKAGES:BOOL=ON \
             -DTrilinos_ENABLE_Gtest:BOOL=OFF \
             -DTrilinos_ENABLE_TESTS=OFF \
             -DTPL_ENABLE_gtest:BOOL=OFF \
             -DTPL_ENABLE_MPI:BOOL=ON \
             -DTPL_ENABLE_HDF5:BOOL=ON \
             -DCMAKE_INSTALL_PREFIX:PATH=/usr \
             -DBUILD_SHARED_LIBS:BOOL=ON
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
