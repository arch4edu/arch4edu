# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dolfinx
pkgdesc="Next generation FEniCS problem solving environment"
pkgver=0.5.1
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${pkgname}"
license=(LGPL3)
makedepends=(cmake)
depends=(boost python-fenics-ffcx hdf5-openmpi parmetis petsc pugixml)
optdepends=('adios2: for use ADIOS2 writer'
  'slepc: for use SLEPc eigen solver'
  'scotch: for compute graph partition'
  'kahip: for compute graph partition in parallel')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('2394f3650923723e9a81643f5e1d42ae03e58274872921daeb182c5b99b8e755d91217d9e05fb3d301c8f7cbce3faff84f233232c7d91b541fd405a359b06ea4')

prepare() {
  sed -i '8 a #include <algorithm>' ${pkgname}-${pkgver}/cpp/${pkgname}/common/MPI.h
}

build() {
  cmake \
    -S ${pkgname}-${pkgver}/cpp \
    -B build-cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -Wno-dev
  cmake --build build-cmake --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build-cmake --target install
  install -Dm 644 ${pkgname}-${pkgver}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
