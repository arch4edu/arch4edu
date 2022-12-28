# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Samuel Williams <samuel.williams@oriontransfer.co.nz>
pkgname=scotch
pkgver=7.0.2
pkgrel=1
pkgdesc="Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering. This is the all-inclusive version (MPI/serial/esmumps)."
url="https//gitlab.inria.fr/scotch/scotch"
license=("custom:CeCILL-C")
depends=('zlib' 'openmpi' 'bzip2')
makedepends=('gcc-fortran' 'cmake')
provides=('ptscotch' 'ptscotch-openmpi' 'scotch_esmumps' 'scotch_ptesmumps')
conflicts=('ptscotch-openmpi' 'scotch_esmumps' 'scotch_esmumps5')
arch=('i686' 'x86_64')
source=("https://gitlab.inria.fr/scotch/scotch/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('17db72097dea75522570fe26ece62d99d480a2ea49954181d87b3e1dc913e05b')

options=(!emptydirs)

prepare(){
  sed -i 's/DESTINATION man/DESTINATION share\/man/g' ${pkgname}-v${pkgver}/CMakeLists.txt
}

build() {
  cmake -S ${pkgname}-v${pkgver} -B build -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DINSTALL_METIS_HEADERS=OFF
  cmake --build build --parallel
}

check() {
  if [ -z $(ldconfig -p | grep libcuda.so.1) ]; then
    export _libcuda=0
  fi
  cmake --build build --parallel --target test
}

package() {
  DESTDIR=${pkgdir} cmake --install build
  # To avoid conflict with extra/gpart, maybe move the package to /opt/scotch ?
  install -m 644 -D "${pkgname}-v${pkgver}/doc/CeCILL-C_V1-en.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

