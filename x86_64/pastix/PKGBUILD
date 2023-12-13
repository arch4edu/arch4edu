# Maintainer: Jakub Klinkovský <lahwaacz@archlinux.org>
# Contributor: Myles English <myles at tdma dot co>

pkgname=pastix
pkgver=6.3.2
pkgrel=1
pkgdesc="High performance parallel solver for very large sparse linear systems based on direct methods"
arch=('x86_64')
url="https://gitlab.inria.fr/solverstack/pastix"
license=('LGPL3')
depends=('cblas' 'lapacke' 'hwloc' 'scotch' 'metis' 'openmpi' 'python')
makedepends=('gcc-fortran' 'cmake' 'ninja' 'doxygen')
provides=('libpastix.so' 'libpastix_kernels.so'
          # also provide the SpM library (internal module)
          'libspm.so' 'libspmf.so')
source=("https://files.inria.fr/pastix/releases/v${pkgver%%.*}/pastix-${pkgver}.tar.gz")
sha256sums=('c4da8802d1933eecf8c09d7e63c014c81ccf353fe623142e9f5c5fc65ed82ee0')

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

    # fix fucked up Python install path
    local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    install -dm755 "${pkgdir}/${site_packages}"
    mv "${pkgdir}"/usr/lib/python./* "${pkgdir}/${site_packages}"
    rmdir "${pkgdir}/usr/lib/python."
}
