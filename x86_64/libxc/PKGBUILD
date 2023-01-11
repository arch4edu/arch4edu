# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=6.1.0
pkgrel=1
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=('i686' 'x86_64' 'aarch64')
url="https://www.tddft.org/programs/${pkgname}"
license=('MPL2')
depends=(python-numpy)
makedepends=(gcc-fortran cmake)
source=(${url}/down.php?file=${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('46d31c7994988fd436c2ff20400ab8afbb10e01b7e5ab24773400f0ea31af517f93c56b571effe1ae2e511302e7c36f54592e43669f8fdc389cb075957a629aa')
options=(staticlibs)

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=ON \
    -DENABLE_FORTRAN=ON \
    -DENABLE_GENERIC=ON \
    -DENABLE_PYTHON=ON \
    -DENABLE_XHOST=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -Wno-dev
  cmake --build build --target all
}

check() {
  ctest --output-on-failure --test-dir build
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
