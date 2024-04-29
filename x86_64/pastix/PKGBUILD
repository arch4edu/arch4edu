# Maintainer: Jakub Klinkovský <lahwaacz at archlinux dot org>
# Contributor: Myles English <myles at tdma dot co>

pkgname=pastix
pkgver=6.3.2
pkgrel=4
pkgdesc="High performance parallel solver for very large sparse linear systems based on direct methods"
arch=(x86_64)
url="https://gitlab.inria.fr/solverstack/pastix"
license=(LGPL-3.0-only)
depends=('cblas' 'lapacke' 'hwloc' 'scotch' 'metis' 'openmpi' 'python')
makedepends=('gcc-fortran' 'cmake' 'ninja' 'doxygen' 'git')
provides=('libpastix.so' 'libpastix_kernels.so'
          # also provide the SpM library (internal module)
          'libspm.so' 'libspmf.so')
source=("https://files.inria.fr/pastix/releases/v${pkgver%%.*}/pastix-${pkgver}.tar.gz"
        "$pkgname-python-path.diff::https://gitlab.inria.fr/solverstack/pastix/-/commit/b53510abc1e363a360d5dfe77110e40150500061.diff"
        "$pkgname-spm-python-path.diff::https://gitlab.inria.fr/solverstack/spm/-/commit/c39966c8917fde748fd54eeb01ad47d318d82095.diff")
sha256sums=('c4da8802d1933eecf8c09d7e63c014c81ccf353fe623142e9f5c5fc65ed82ee0'
            'de4286abc0b97ff29e644aeff562ccdbd0b4a4a5703fb96edb60e5afa8e38daa'
            '3300759ae59439ca3e678aca9c949b740836fe2e87eb20f9a93d493d74e969d0')

prepare() {
    cd "${pkgname}-${pkgver}"
    git apply -p1 --exclude spm ../$pkgname-python-path.diff
    cd spm
    git apply -p1 ../../$pkgname-spm-python-path.diff
}

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
