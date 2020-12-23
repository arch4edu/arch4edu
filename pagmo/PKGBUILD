# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Joey Dumont <joey.dumont@gmail.com>

pkgname=pagmo
pkgver=2.16.1
pkgrel=1
pkgdesc="Perform parallel computations of optimisation tasks (global and local) via the asynchronous generalized island model"
arch=('i686' 'x86_64')
url="https://github.com/esa/pagmo2"
license=('GPLv3')
depends=('boost' 'intel-tbb' 'coin-or-ipopt' 'eigen' 'nlopt')
makedepends=('cmake')
_name=pagmo2
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/esa/${_name}/archive/v${pkgver}.tar.gz")
sha256sums=('45f2039f2198b6edadf81bdefb10a228f9dd087940c1f1ab1882098f16581df0')

build() {
    mkdir -p "${srcdir}/${_name}-${pkgver}-build"
    cd "${srcdir}/${_name}-${pkgver}-build"

    cmake \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DPAGMO_WITH_IPOPT=ON \
        -DPAGMO_WITH_EIGEN3=ON \
        -DPAGMO_WITH_NLOPT=ON \
        "${srcdir}/${_name}-${pkgver}"

    make
}

package() {
    cd "${srcdir}/${_name}-${pkgver}-build"
    make DESTDIR="${pkgdir}/" install
}
