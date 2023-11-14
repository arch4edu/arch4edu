# Maintainer: Jakub Klinkovský <lahwaacz@archlinux.org>
# Contributor: Myles English <myles at tdma dot co>

pkgname=pastix
pkgver=6.3.0
pkgrel=5
pkgdesc="High performance parallel solver for very large sparse linear systems based on direct methods"
arch=('x86_64')
url="https://gitlab.inria.fr/solverstack/pastix"
license=('LGPL3')
depends=('cblas' 'lapacke' 'hwloc' 'scotch' 'metis' 'openmpi' 'python')
makedepends=('gcc-fortran' 'cmake' 'ninja' 'doxygen')
provides=('libpastix.so' 'libpastix_kernels.so'
          # also provide the SpM library (internal module)
          'libspm.so' 'libspmf.so')
source=("https://files.inria.fr/pastix/releases/v6/pastix-6.3.0.tar.gz")
sha256sums=('a6bfec32a3279d7b24c5fc05885c6632d177e467f1584707c6fd7c42a8703c3e')

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

    # remove the env script (not necessary since we install into /usr which is searched by default)
    rm "${pkgdir}/usr/bin/pastix_env.sh"
    # remove the completion script (useless since this package does not install anything in bin/)
    rm "${pkgdir}/usr/bin/pastix_completion.sh"
    # remove empty directory
    rmdir "${pkgdir}/usr/bin"

    # move examples into proper doc directory
    install -dm755 "${pkgdir}/usr/share/doc/pastix/"
    mv "${pkgdir}/usr/examples" "${pkgdir}/usr/share/doc/pastix/"

    # fix fucked up Python install path
    local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    install -dm755 "${pkgdir}/${site_packages}"
    mv "${pkgdir}"/usr/lib/python/* "${pkgdir}/${site_packages}"
    rmdir "${pkgdir}/usr/lib/python"
}
