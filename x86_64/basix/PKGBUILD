# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=basix
pkgdesc="FEniCS finite element basis evaluation library"
pkgver=0.9.0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${pkgname}"
license=(MIT)
depends=(gcc-libs lapack)
makedepends=(cmake doxygen texlive-plaingeneric texlive-fontsrecommended texlive-latexextra)
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0ea49f7710265ef7d3d61607285c263b923265af8d1435ebeb557f26281bca593a1ee711c2c3f3bf97048cb5e226e574279f22fd2c6d3898e4f1e5b48251f806')

build() {
  cmake \
    -S ${pkgname}-${pkgver}/cpp \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_CXX_COMPILER=g++ \
    -DINSTALL_RUNTIME_DEPENDENCIES=OFF \
    -Wno-dev
  cmake --build build --target all

  cd ${srcdir}/${pkgname}-${pkgver}/doc/cpp
  doxygen -u Doxyfile
  doxygen .
  cd latex
  make
}

check() {
  DESTDIR="${PWD}/tmp_install" cmake --build build --target install
  CMAKE_PREFIX_PATH="${srcdir}/tmp_install/usr/lib/cmake/${pkgname}" cmake \
    -S ${pkgname}-${pkgver}/test/test_cmake \
    -B build_test
  cmake --build build_test
  build_test/a.out

  CMAKE_PREFIX_PATH="${srcdir}/tmp_install/usr/lib/cmake/${pkgname}" cmake \
    -S ${pkgname}-${pkgver}/demo/cpp/demo_create_and_tabulate \
    -B build_demo_create_and_tabulate
  cmake --build build_demo_create_and_tabulate
  build_demo_create_and_tabulate/demo_create_and_tabulate

  CMAKE_PREFIX_PATH="${srcdir}/tmp_install/usr/lib/cmake/${pkgname}" cmake \
    -S ${pkgname}-${pkgver}/demo/cpp/demo_dof_transformations \
    -B build_demo_dof_transformations
  cmake --build build_demo_dof_transformations
  build_demo_dof_transformations/demo_dof_transformations
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -d ${pkgdir}/usr/share/doc/${pkgname}
  mv ${pkgname}-${pkgver}/doc/cpp/html ${pkgdir}/usr/share/doc/${pkgname}
  install ${pkgname}-${pkgver}/doc/cpp/latex/*.pdf ${pkgdir}/usr/share/doc/${pkgname}
  install -Dm 644 ${pkgname}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
