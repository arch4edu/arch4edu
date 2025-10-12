# Maintainer: Valentina Schüller <valentina.schueller@mailbox.org>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Florian Lindner <florian.lindner@xgm.de>

pkgname=precice
pkgver=3.3.0
pkgrel=1
pkgdesc="A Coupling Library for Partitioned Multi-Physics Simulations on Massively Parallel Systems"
arch=(x86_64)
url="https://${pkgname}.org"
license=(LGPL-3.0-or-later)
depends=(boost libxml2 openmpi petsc python-numpy)
conflicts=(petsc-complex)
makedepends=(cmake eigen gcc-fortran)
optdepends=('man-db: manual pages for precice-tools'
  'git: for Git Revision Info support')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/${pkgname}/${pkgname}/archive/v${pkgver}.tar.gz)
sha512sums=('eea9bfa340c84dfca1523eb1282f624c14abe46d788b416b88460a90fe12f605f92d7838c51d0d184f1d40e7997427af24a18b44c6be383d84a94df3ec826419')

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
