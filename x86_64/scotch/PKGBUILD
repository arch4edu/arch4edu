# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Samuel Williams <samuel.williams@oriontransfer.co.nz>
pkgname=scotch
pkgver=7.0.7
pkgrel=2
pkgdesc="Package for graph, mesh/hypergraph partitioning, static mapping, and sparse matrix block ordering"
url="https://gitlab.inria.fr/scotch/scotch"
license=('CECILL-C')
depends=('zlib' 'openmpi' 'bzip2' 'xz')
makedepends=('gcc-fortran' 'cmake')
provides=('ptscotch' 'ptscotch-openmpi' 'scotch_esmumps' 'scotch_ptesmumps')
conflicts=('ptscotch-openmpi' 'scotch_esmumps' 'scotch_esmumps5')
arch=('i686' 'x86_64')
source=("https://gitlab.inria.fr/scotch/scotch/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha512sums=('5369e5fdca605bd0db837b34a3d8feb6f9a67f3dc7c6e14ee0e389c5436cb245c5e842546b8997d4a5466fed1dbaaaa8e0531a5dbe68b995d4975bd8723ac1f1')

options=(!emptydirs)

prepare(){
  sed -i 's/if(CMAKE_C_COMPILER_ID STREQUAL "GNU")/if(CMAKE_C_COMPILER_ID STREQUAL "GNUXX")/g' ${pkgname}-v${pkgver}/src/CMakeLists.txt # fix for 7.0.7
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
  DESTDIR=${pkgdir} cmake --install build
  mv ${pkgdir}/usr/bin/gpart ${pkgdir}/usr/bin/gpart_scotch # avoid conflict with extra/gpart
  install -d ${pkgdir}/usr/share/licenses/scotch
  install -Dm644 ${pkgname}-v${pkgver}/doc/CeCILL-C_V1-*.txt ${pkgdir}/usr/share/licenses/scotch
}

