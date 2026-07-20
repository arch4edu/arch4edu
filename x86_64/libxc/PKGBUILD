# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=7.1.1
pkgrel=1
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=(i686 x86_64 aarch64)
url="https://${pkgname}.gitlab.io"
license=(MPL-2.0)
depends=(python-numpy)
makedepends=(gcc-fortran cmake python-pytest)
source=(https://gitlab.com/${pkgname}/${pkgname}/-/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('93945ca4b02a6ca7224f895286109bc4ed434d54e7b6ef713142c71b5ca0028e6fe6d377b07a6c7574df729eacc5f186a32485cc35eed44fa22949be7950f877')
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
