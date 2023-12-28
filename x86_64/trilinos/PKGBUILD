# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Gianluca Pettinello <g_pet@hotmail.com>
# Contributor: Alad Wenter <alad@archlinux.org>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>
pkgname=trilinos
pkgver=15.0.0
_pkgver=${pkgver//./-}
pkgrel=2
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
sha512sums=('a364e67686cdd4e1e34aa0e14b6cc051ed21a72b63719c47260d7839d47590b9e652be76cb9d61e513c7933b965fc8141c3ff898167e22353b33c9491a525c84'
            'cccd319861b33b9e809e6bee3a11f5f8604dbb765b9c074b0c02cb941231f621dc332eab58fcb07d4e291150be3372d0e58b4916de98b5a01b096a9ad5e5cfe8')

prepare() {
  patch -d  Trilinos-trilinos-release-"$_pkgver" -p1 -i ../compiler-errors.patch
}

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
