# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=5.2.3
pkgrel=1
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=('i686' 'x86_64' 'aarch64')
url="https://www.tddft.org/programs/${pkgname}"
license=('MPL2')
depends=(python-numpy)
makedepends=(gcc-fortran cmake)
source=(${url}/down.php?file=${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('e7a5100af2a4a1d0aee773919cca31bfffdc2a8c0a04d9df9247df5ec78a9ef13d1da9585cc6e3f3f96f6a974cafc762493d66d2fd7dea312b9e0f4dee3c934f')
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
