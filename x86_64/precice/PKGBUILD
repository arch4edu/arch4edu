# Maintainer: Valentina Schüller <valentina.schueller@mailbox.org>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Florian Lindner <florian.lindner@xgm.de>

pkgname=precice
pkgver=3.5.0
pkgrel=1
pkgdesc="A Coupling Library for Partitioned Multi-Physics Simulations on Massively Parallel Systems"
arch=(x86_64)
url="https://${pkgname}.org"
license=(LGPL-3.0-or-later)
depends=(boost boost-libs libxml2 openmpi petsc python-numpy)
conflicts=(petsc-complex)
makedepends=(cmake eigen gcc-fortran)
optdepends=('man-db: manual pages for precice-tools'
  'git: for Git Revision Info support')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/${pkgname}/${pkgname}/archive/v${pkgver}.tar.gz)
sha512sums=('b633485ce8e49cf6d7adffc24e0f58e7aede0e1f81f81d5c0af870d5fe4a7c3f2c878c011bb359671857e0ff507f2f296677ff47826066c11bcb0ea5173ea2ab')

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_STANDARD=17 \
    -DBUILD_SHARED_LIBS=ON \
    -DPRECICE_FEATURE_MPI_COMMUNICATION=ON \
    -DPRECICE_FEATURE_PETSC_MAPPING=ON \
    -DPRECICE_FEATURE_PYTHON_ACTIONS=ON \
    -DPRECICE_CONFIGURE_PACKAGE_GENERATION=ON \
    -DPRECICE_FEATURE_GINKGO_MAPPING=OFF \
    -DPRECICE_BINDINGS_C=ON \
    -DPRECICE_BINDINGS_FORTRAN=ON \
    -DPRECICE_BUILD_TOOLS=ON \
    -Wno-dev

  cmake --build build
}

# check() {
#   ctest --test-dir build
# }

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm 644 ${pkgname}-${pkgver}/LICENSE -t ${pkgdir}/usr/share/licenses/${pkgname}
  install -Dm 644 ${pkgname}-${pkgver}/docs/man/man1/${pkgname}-tools.1 -t ${pkgdir}/usr/share/man/man1
  cd "${pkgdir}"
  rm -r usr/share/lintian
}
