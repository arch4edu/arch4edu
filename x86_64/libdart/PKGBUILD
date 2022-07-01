# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Gonçalo Camelo Neves Pereira <goncalo_pereira@outlook.pt>
# Contributor: midgard <arch dot midgard "at symbol" janmaes "youknowwhat" com>

pkgname=libdart
pkgver=6.12.1
pkgrel=2
pkgdesc="Dynamic Animation and Robotics Toolkit"
arch=('i686' 'x86_64')
url="https://dartsim.github.io"
license=('BSD')
depends=('assimp' 'boost' 'eigen' 'fcl' 'libccd' 'bullet' 'coin-or-ipopt'
         'nlopt' 'octomap' 'ode' 'openscenegraph' 'tinyxml2' 'urdfdom'
         'glu' 'freeglut' 'libxi' 'libxmu' 'pagmo')
optdepends=('pagmo: pagmo optimizer support')
makedepends=('cmake')
provides=('dartsim')
_pkgname=dart
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dartsim/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('e0d47bbc191903b93474da00bbd1042cefdc85f5ead3e9a9282b5f4187d53304')

# Make libdart use pagmo 2.18.0 instead of 2.17.0
prepare(){
    sed -i '9s/7/8/' ${srcdir}/${_pkgname}-${pkgver}/cmake/DARTFindpagmo.cmake
}

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
