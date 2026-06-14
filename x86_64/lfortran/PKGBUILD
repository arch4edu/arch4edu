# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Ciappi <marco.scopesi@gmail.com>
pkgname=lfortran
pkgver=0.63.0
pkgrel=2
pkgdesc="Modern interactive LLVM-based Fortran compiler"
arch=(x86_64)
url="https://${pkgname}.org"
license=(BSD-3-Clause)
depends=(clang kokkos zlib ncurses xeus-zmq)
makedepends=(llvm cmake cppzmq zstd libunwind pandoc-cli re2c)
checkdepends=()
optdepends=()
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/${pkgname}/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('317cca18dcc98287b750095f8c2bee6150b85e5d792c48804f6da441c7a48fb0dfda61bbb48b61187234b995f574f2c1e5dcd9657d84e04ae3ad10dfaed88400')

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=17 \
    -DWITH_LLVM=yes \
    -DWITH_RUNTIME_LIBRARY=yes \
    -DWITH_XEUS=yes \
    -DWITH_KOKKOS=yes \
    -DWITH_ZLIB=yes \
    -DWITH_ZSTD=yes \
    -DUSE_DYNAMIC_ZSTD=yes \
    -Wno-dev

  cmake --build build --target all
}

check() {
  ctest --verbose --output-on-failure --test-dir build
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
