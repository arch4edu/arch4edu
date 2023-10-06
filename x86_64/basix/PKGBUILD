# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=basix
pkgdesc="FEniCS finite element basis evaluation library"
pkgver=0.7.0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${pkgname}"
license=(MIT)
depends=(lapack)
makedepends=(cmake)
checkdepends=(python)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('6d4981e31f5e476a3baefbcee1ccdf182a0723a02d2fd1582c9f26c75e1c215e7a25647af3dc385562ca5a35088bed263c5bffc19a15812001ccb3ed8c2f426b')

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
