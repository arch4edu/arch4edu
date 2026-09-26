pkgname=pagmo
pkgver=2.20.0
pkgrel=1
pkgdesc="Perform parallel computations of optimisation tasks (global and local) via the asynchronous generalized island model"
arch=('x86_64')
url="https://github.com/esa/pagmo2"
license=('GPLv3')
depends=('boost-libs' 'onetbb' 'coin-or-ipopt' 'eigen' 'nlopt')
makedepends=('cmake' 'boost')
_name=pagmo2
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/esa/${_name}/archive/v${pkgver}.tar.gz")
sha256sums=('8d684e9a3667dcccc844489083906c35aba7610594c5fce0f4eccce9c2264f4d')

prepare() {
  cd "${srcdir}/pagmo2-$pkgver"
}

build() {
    cd "${srcdir}"/${_name}-${pkgver}
    cmake \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_UNITY_BUILD=ON \
        -DPAGMO_WITH_IPOPT=ON \
        -DPAGMO_WITH_EIGEN3=ON \
        -DPAGMO_WITH_NLOPT=ON \
        -B build .
    cmake --build build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    DESTDIR="${pkgdir}/" cmake --build build --target install
}
