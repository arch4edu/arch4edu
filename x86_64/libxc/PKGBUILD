# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: James Spencer <james.s.spencer@gmail.com>
# Contributor: Anton Kudelin <kudelin at protonmail dot com>
pkgname=libxc
pkgver=7.0.0
pkgrel=2
pkgdesc="A library of exchange-correlation functionals for density-functional theory"
arch=(i686 x86_64 aarch64)
url="https://${pkgname}.gitlab.io"
license=(MPL-2.0)
depends=(python-numpy)
makedepends=(gcc-fortran cmake)
source=(https://gitlab.com/${pkgname}/${pkgname}/-/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz
cmake.patch::https://gitlab.com/${pkgname}/${pkgname}/-/merge_requests/696.patch)
sha512sums=('ae50760cb4afb37af26cbc5cf819d1bfaa2fa1fc01509b73a4e2533ca772cff5750493974f63f573cf5748ed1007e21c7611d3840b3fa50a3e77e74f7a027988'
            'e3b6e45ff38f6bc5053bcdcb1c1d7fc65bf24fd148728abceaad770fe396d2a1a155d17f196199cca60ce62070cb331052a4687960731a8e0c4b261578b1108b')
options=(staticlibs)

prepare() {
  cd ${pkgname}-${pkgver}
  patch -p1 -i ../cmake.patch
}

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
