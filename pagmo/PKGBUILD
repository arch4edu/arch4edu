# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Joey Dumont <joey.dumont@gmail.com>

pkgname=pagmo
pkgver=2.16.0
pkgrel=3
pkgdesc="Perform parallel computations of optimisation tasks (global and local) via the asynchronous generalized island model"
arch=('i686' 'x86_64')
url="https://github.com/esa/pagmo2"
license=('GPLv3')
depends=('boost' 'intel-tbb' 'coin-or-ipopt' 'eigen' 'nlopt')
makedepends=('cmake')
_name=pagmo2
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/esa/${_name}/archive/v${pkgver}.tar.gz"
        "ipopt.patch::https://github.com/esa/pagmo2/commit/4ba6b6b68339c3905b8b58857e71822527e224fd.patch"
        "cxx_std_17.patch::https://github.com/esa/pagmo2/commit/e24fe9336e69ace4f180e49643a86f93652d162c.patch")
sha256sums=('076918ca975e2b45eedd85b65da0de650d4bd0b3f86182c0c144c7fdc191185b'
            '11edcdacfcd36b4c38d0a479266894b9788ea655f875eb243a85cb5ea062ad52'
            'd70fb9ec84fc6aa55120d0a2e68812aafec45cbfb07b6b81578a0be86b905876')

prepare() {
    cd "${srcdir}/${_name}-${pkgver}"
    patch -Np1 -i "${srcdir}"/ipopt.patch
    patch -Np1 -i "${srcdir}"/cxx_std_17.patch
}

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
