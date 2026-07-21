# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=7.1.2
pkgrel=1
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=(i686 x86_64 aarch64)
url="https://${pkgname}.gitlab.io"
license=(MPL-2.0)
depends=(python-numpy)
makedepends=(gcc-fortran cmake python-pytest)
source=(https://gitlab.com/${pkgname}/${pkgname}/-/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('660339cadc6838308feed1db1eb25a0bd09dd1673398a1bc0682557e9aed08d871cdf5d75a6914760e1479459490cd4aea6e4b97663eaf317322832605bf34a6')
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
