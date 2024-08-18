# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Samuel Williams <samuel.williams@oriontransfer.co.nz>
pkgname=scotch
pkgver=7.0.5
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
sha512sums=('9566ca800fd47df63844df6ff8b0fbbe8efbdea549914dfe9bf00d3d104a8c5631cfbef69e2677de68dcdb93addaeed158e6f6a373b5afe8cec82ac358946b65')

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
        -D COMMON_PTHREAD_AFFINITY_LINUX:BOOL=ON
  make -C build
}

check() {
  make -C build test
}

package() {
  # To avoid conflict with extra/gpart, maybe move the package to /opt/scotch ?
  DESTDIR=${pkgdir} cmake --install build
}

