# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dumux-precice
pkgver=2.0.0
pkgrel=2
pkgdesc="DuMuX-preCICE adapter"
arch=(x86_64)
url="https://github.com/precice/${pkgname/precice/adapter}"
license=(GPL-3.0-or-later)
depends=(dumux precice)
source=(${pkgname/precice/adapter}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('466f685641619c734149d19e40b270872b70818041f0bfd2b10d0ea9f33c8e4ebfb822708fa7db25eabfd8d3f645fbc9c36caa0047772947c6bb3d18bead2e3f')

prepare() {
  sed -i 's/DumuxPreciceTestMacros.cmake/#DumuxPreciceTestMacros.cmake/' ${pkgname/precice/adapter}-${pkgver}/cmake/modules/CMakeLists.txt
  sed -i '2 a	\ \ \ \ \ \ \ \ dumuxpreciceindexmapper.hh' ${pkgname/precice/adapter}-${pkgver}/${pkgname}/CMakeLists.txt
  # https://stackoverflow.com/a/50949315/9302545
  sed -i 's/return/exit/' ${pkgname/precice/adapter}-${pkgver}/test/return-test-passed.sh
}

build() {
  cmake \
    -S ${pkgname/precice/adapter}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_FLAGS='-Wall -fdiagnostics-color=always' \
    -DCMAKE_CXX_FLAGS="-Wall -fdiagnostics-color=always -mavx" \
    -DCMAKE_POSITION_INDEPENDENT_CODE=TRUE \
    -DENABLE_HEADERCHECK=ON \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname/precice/adapter}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}
