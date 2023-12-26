# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Samuel Williams <samuel.williams@oriontransfer.co.nz>
pkgname=scotch
pkgver=7.0.4
pkgrel=2
pkgdesc="Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering. This is the all-inclusive version (MPI/serial/esmumps)."
url="https://gitlab.inria.fr/scotch/scotch"
license=("custom:CeCILL-C")
depends=('zlib' 'openmpi' 'bzip2')
makedepends=('gcc-fortran' 'cmake' 'flex' 'bison')
provides=('ptscotch' 'ptscotch-openmpi' 'scotch_esmumps' 'scotch_ptesmumps')
conflicts=('ptscotch-openmpi' 'scotch_esmumps' 'scotch_esmumps5')
arch=('i686' 'x86_64')
source=("https://gitlab.inria.fr/scotch/scotch/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha512sums=('7c2a770c8b0932372a01613668d200fb934596df76293c7ed0e51ed8c1b57447d441937d98a2ad1d53e5579c0320d499910e7b1451b319c2acd9bcc56e6cfac3')

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
  if [ -z "$(ldconfig -p | grep libcuda.so.1)" ]; then
    export _libcuda=0
  fi
  make -C build test
}

package() {
  DESTDIR=${pkgdir} cmake --install build
  # To avoid conflict with extra/gpart, maybe move the package to /opt/scotch ?
  install -m 644 -D "${pkgname}-v${pkgver}/doc/CeCILL-C_V1-en.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

