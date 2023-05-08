# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=basix
pkgdesc="FEniCS finite element basis evaluation library"
pkgver=0.6.0
pkgrel=2
arch=(x86_64)
url="https://github.com/FEniCS/${pkgname}"
license=(MIT)
depends=(lapack)
makedepends=(cmake)
checkdepends=(python)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('265be90be0790f0e5e2d5122ed5455bf0f3bf8ab359ccdc63f9a36c08f64fbc82cf2954a2a769f58bf1427232fe49b14764d7b3153e038f42036f98e5597c1de')

prepare() {
  # gcc-13-compatibilty
  sed -i '/#include <vector>/a #include <cstdint>' ${pkgname}-${pkgver}/cpp/basix/finite-element.h
}

build() {
  cmake \
    -S ${pkgname}-${pkgver}/cpp \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_CXX_COMPILER=g++ \
    -Wno-dev
  cmake --build build --target all
}

check() {
  DESTDIR="${PWD}/tmp_install" cmake --build build --target install
  CMAKE_PREFIX_PATH="${srcdir}/tmp_install/usr/lib/cmake/${pkgname}" cmake \
    -S ${pkgname}-${pkgver}/test/test_cmake \
    -B build_test
  cmake --build build_test
  build_test/a.out
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
