# Maintainer: Jakub Klinkovský <lahwaacz@archlinux.org>
# Contributor: Myles English <myles at tdma dot co>

pkgname=pastix
pkgver=6.3.1
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
sha256sums=('290464d73b7d43356e4735a29932bf6f23a88e94ec7139ba7744c21e42c52681')

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

prepare() {
    cd "${pkgname}-${pkgver}"
    # version 6.3.1 temporarily replaces "-Werror" for one check, but it leaves
    # "=format-security" in there from the "-Werror=format-security" flag
    sed -i '/-Werror/d' spm/cmake_modules/morse_cmake/modules/find/FindM.cmake
    sed -i '/-Werror/d' cmake_modules/morse_cmake/modules/find/FindM.cmake
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
    mv "${pkgdir}/usr/examples/"* "${pkgdir}/usr/share/doc/pastix/examples/"
    rmdir "${pkgdir}/usr/examples/"

    # fix fucked up Python install path
    local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    install -dm755 "${pkgdir}/${site_packages}"
    mv "${pkgdir}"/usr/lib/python/* "${pkgdir}/${site_packages}"
    rmdir "${pkgdir}/usr/lib/python"
}
