# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Samuel Williams <samuel.williams@oriontransfer.co.nz>
pkgname=scotch
pkgver=7.0.6
pkgrel=1
pkgdesc="Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering"
url="https://gitlab.inria.fr/scotch/scotch"
license=('CECILL-C')
depends=('zlib' 'openmpi' 'bzip2' 'xz')
makedepends=('gcc-fortran' 'cmake')
provides=('ptscotch' 'ptscotch-openmpi' 'scotch_esmumps' 'scotch_ptesmumps')
conflicts=('ptscotch-openmpi' 'scotch_esmumps' 'scotch_esmumps5')
arch=('i686' 'x86_64')
source=("https://gitlab.inria.fr/scotch/scotch/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha512sums=('781d906f8084c9e27a4179c888e8c24d4e4807e18608cdc20cfeef7990c687b5957a6866382f23a9ad995351ba2f30c182f3198c3cbe7c2eed8ff701719eebca')

options=(!emptydirs)

prepare(){
  sed -i 's/DESTINATION man/DESTINATION share\/man/g' ${pkgname}-v${pkgver}/CMakeLists.txt
}

build() {
  cmake -S ${pkgname}-v${pkgver} \
        -B build \
        -D CMAKE_INSTALL_PREFIX:PATH=/usr \
        -D CMAKE_BUILD_TYPE:STRING=Release \
        -D BUILD_SHARED_LIBS:BOOL=ON \
        -D INSTALL_METIS_HEADERS:BOOL=OFF \
        -D COMMON_PTHREAD_FILE:BOOL=ON \
        -D SCOTCH_PTHREAD:BOOL=ON \
        -D SCOTCH_PTHREAD_MPI:BOOL=ON \
        -D COMMON_PTHREAD_AFFINITY_LINUX:BOOL=ON \
        -D CMAKE_C_FLAGS:STRING="${CFLAGS} -Wp,-D_FORTIFY_SOURCE=2" \
        -D CMAKE_CXX_FLAGS:STRING="${CXXFLAGS} -Wp,-D_FORTIFY_SOURCE=2"
  make -C build
}

check() {
  make -C build test
}

package() {
  # To avoid conflict with extra/gpart, maybe move the package to /opt/scotch ?
  DESTDIR=${pkgdir} cmake --install build
}

