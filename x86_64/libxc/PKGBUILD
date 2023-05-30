# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=6.2.0
pkgrel=1
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=('i686' 'x86_64' 'aarch64')
url="https://www.tddft.org/programs/${pkgname}"
license=('MPL2')
depends=(python-numpy)
makedepends=(gcc-fortran cmake)
#source=(${url}/down.php?file=${pkgver}/${pkgname}-${pkgver}.tar.gz)
source=(https://gitlab.com/${pkgname}/${pkgname}/-/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('924eccabf75972e066f7550967516eccca3d02ec672027de02fcb86e0cdb5b8e30a03424f8c1531ce3c5ed98ab7c310005e3163a6670c0a9524c51129556b525')
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
