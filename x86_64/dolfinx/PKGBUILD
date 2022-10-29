# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dolfinx
pkgdesc="Next generation FEniCS problem solving environment"
pkgver=0.5.2
pkgrel=2
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
sha512sums=('c6a9af8abc37172493a547ff52a3d737bf16b34f35d737d3643b0d7578455e6097eca6c919b49bbfacfed165b028170a1d55a7cf7521e285612f1f9fc7c55522')

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
