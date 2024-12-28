# Maintainer: Jakub Klinkovský <lahwaacz at archlinux dot org>
# Contributor: Myles English <myles at tdma dot co>

pkgname=pastix
pkgver=6.4.0
pkgrel=2
pkgdesc="High performance parallel solver for very large sparse linear systems based on direct methods"
arch=(x86_64)
url="https://gitlab.inria.fr/solverstack/pastix"
license=(LGPL-3.0-only)
depends=('cblas' 'lapacke' 'hwloc' 'scotch' 'metis' 'openmpi' 'python')
makedepends=('gcc-fortran' 'cmake' 'ninja' 'doxygen' 'git')
provides=('libpastix.so' 'libpastix_kernels.so'
          # also provide the SpM library (internal module)
          'libspm.so' 'libspmf.so')
source=("https://files.inria.fr/pastix/releases/v${pkgver%%.*}/pastix-${pkgver}.tar.gz")
sha256sums=('891d426188eed56c1075fb34d2d80132593a1536ffc05cf333567f68a4811e55')

build() {
    cmake -B build -S "${pkgname}-${pkgver}" -G Ninja \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_SHARED_LIBS=ON \
        -DBUILD_DOCUMENTATION=ON \
        -DPASTIX_ORDERING_METIS=ON \
        -DPASTIX_WITH_MPI=ON \
        -DPASTIX_INT64=OFF   # because scotch is not compiled with int64
    cmake --build build
}

package() {
    DESTDIR="${pkgdir}" cmake --install build
}
