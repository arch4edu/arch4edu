# Maintainer: Jakub Klinkovský <j.l.k cat gmx dog com>
# Contributor: Myles English <myles at tdma dot co>

pkgname=pastix
pkgver=6.2.2
pkgrel=1
pkgdesc="High performance parallel solver for very large sparse linear systems based on direct methods"
arch=('x86_64')
url="https://gitlab.inria.fr/solverstack/pastix"
license=('LGPL3')
depends=('cblas' 'lapacke' 'hwloc' 'scotch' 'metis' 'openmpi' 'python')
makedepends=('gcc-fortran' 'cmake' 'git' 'doxygen')
provides=('libpastix.so' 'libpastix_kernels.so'
          # also provide the SpM library (internal module)
          'libspm.so' 'libspmf.so')
source=("${pkgname}::git+${url}.git#tag=v${pkgver}"
        gitmodules.diff)
md5sums=('SKIP'
         '59430d563cc9a665292c0d793520e148')

prepare() {
    cd "${pkgname}"
    patch -p2 < ../gitmodules.diff
    git submodule update --init --recursive

    # fix for metis-5.1.0.p10-1 https://bugs.archlinux.org/task/70446
    sed -i 's|LIBRARIES metis|LIBRARIES metis m|' cmake_modules/morse_cmake/modules/find/FindMETIS.cmake

    [ -d build ] && rm -rf build
    mkdir build
}

build() {
    cd "${pkgname}/build"
    cmake .. \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_SHARED_LIBS=ON \
        -DBUILD_DOCUMENTATION=ON \
        -DPASTIX_ORDERING_METIS=ON \
        -DPASTIX_WITH_MPI=ON \
        -DPASTIX_INT64=OFF   # because scotch is not compiled with int64
    make
}

package() {
    cd "${pkgname}/build"
    make install DESTDIR="${pkgdir}"

    # remove the env script (not necessary since we install into /usr which is searched by default)
    rm "${pkgdir}/usr/bin/pastix_env.sh"
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
