pkgname=pagmo
pkgver=2.19.1
pkgrel=1
pkgdesc="Perform parallel computations of optimisation tasks (global and local) via the asynchronous generalized island model"
arch=('x86_64')
url="https://github.com/esa/pagmo2"
license=('GPLv3')
depends=('boost' 'tbb' 'coin-or-ipopt' 'eigen' 'nlopt')
makedepends=('cmake')
_name=pagmo2
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/esa/${_name}/archive/v${pkgver}.tar.gz")
sha256sums=('ecc180e669fa6bbece959429ac7d92439e89e1fd1c523aa72b11b6c82e414a1d')

build() {
    cd "${srcdir}"/${_name}-${pkgver}
    cmake \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_UNITY_BUILD=ON \
        -DPAGMO_WITH_IPOPT=ON \
        -DPAGMO_WITH_EIGEN3=ON \
        -DPAGMO_WITH_NLOPT=ON \
        -B build .
    make -C build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}/build"
    make DESTDIR="${pkgdir}/" install
}
