# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=6.2.2
pkgrel=1
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=('i686' 'x86_64' 'aarch64')
url="https://www.tddft.org/programs/${pkgname}"
license=('MPL2')
depends=(python-numpy)
makedepends=(gcc-fortran cmake)
#source=(${url}/down.php?file=${pkgver}/${pkgname}-${pkgver}.tar.gz)
source=(https://gitlab.com/${pkgname}/${pkgname}/-/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('45333424a4569576ab1553128ea2b113df6e6a70740e941bbbca95aa5918d19723e8371c02b60ff7b17d0b7fa2d5cea6cb69cedd58a4700a6a4d42ed93487472')
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
