# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Gonçalo Camelo Neves Pereira <goncalo_pereira@outlook.pt>
# Contributor: midgard <arch dot midgard "at symbol" janmaes "youknowwhat" com>

pkgname=libdart
pkgver=6.11.0
pkgrel=1
pkgdesc="Dynamic Animation and Robotics Toolkit"
arch=('i686' 'x86_64')
url="https://dartsim.github.io"
license=('BSD')
depends=('assimp' 'boost' 'eigen' 'fcl' 'libccd' 'bullet' 'coin-or-ipopt'
         'flann' 'nlopt' 'octomap' 'ode' 'openscenegraph' 'tinyxml2' 'urdfdom'
         'glu' 'freeglut' 'libxi' 'libxmu')
optdepends=('pagmo: pagmo optimizer support')
makedepends=('cmake')
provides=('dartsim')
_pkgname=dart
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dartsim/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('41d783d7f99d7b5ad1874336646f1bdfa33e146e0652a6c32d12eaa21505bd51')

build() {
    mkdir -p "${srcdir}/${_pkgname}-${pkgver}/build"
    cd "${srcdir}/${_pkgname}-${pkgver}/build"

    cmake .. \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_INSTALL_LIBDIR="lib" \

    make
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}/build"

    make DESTDIR="${pkgdir}/" install
}
