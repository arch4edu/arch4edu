# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Gonçalo Camelo Neves Pereira <goncalo_pereira@outlook.pt>
# Contributor: midgard <arch dot midgard "at symbol" janmaes "youknowwhat" com>

pkgname=libdart
pkgver=6.9.5
pkgrel=5
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
sha256sums=('624c00b65e3a753cba50de038620860c86e2ac47b1793ae51f9427a4bcb14c32')

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
