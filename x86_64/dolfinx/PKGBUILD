# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=dolfinx
pkgdesc="Next generation FEniCS problem solving environment"
pkgver=0.10.0.post2
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${pkgname}"
license=(LGPL-3.0-or-later GPL-3.0-or-later)
depends=(adios2 boost kahip parmetis-git pugixml python-fenics-ffcx scotch petsc spdlog) # slepc
makedepends=(cmake doxygen texlive-plaingeneric texlive-fontsrecommended texlive-latexextra)
checkdepends=(catch2)
# optdepends=('adios2: for use ADIOS2 writer'
#   'kahip: for compute graph partition in parallel'
#   'parmetis: for parallel graph partitioning'
#   'slepc: for use SLEPc eigen solver')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('bfc7726169679871ffcb6d44bfbeb4103878d248ead78aca5a84810e4df4741f7dbf689deca091afca0cb3f45658cc1c1d556b29f9d400371daa61348f3373ea')

build() {
  export LDFLAGS="-lkahip $LDFLAGS"

  cmake \
    -S ${pkgname}-${pkgver}/cpp \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DDOLFINX_BASIX_PYTHON=ON \
    -DDOLFINX_ENABLE_ADIOS2=ON \
    -DDOLFINX_ENABLE_PETSC=ON \
    -DDOLFINX_ENABLE_PARMETIS=ON \
    -DDOLFINX_ENABLE_SCOTCH=ON \
    -DDOLFINX_ENABLE_SLEPC=OFF \
    -DDOLFINX_ENABLE_KAHIP=ON \
    -DDOLFINX_SKIP_BUILD_TESTS=OFF \
    -DDOLFINX_UFCX_PYTHON=ON \
    -DINSTALL_RUNTIME_DEPENDENCIES=OFF \
    -Wno-dev
  cmake --build build --target all

  cd ${srcdir}/${pkgname}-${pkgver}/cpp/doc
  doxygen -u Doxyfile
  doxygen .
  cd latex
  make
}

check() {
  ffcx ${pkgname}-${pkgver}/cpp/test/poisson.py -o ${pkgname}-${pkgver}/cpp/test
  DESTDIR="${PWD}/tmp_install" cmake --build build --target install

  CMAKE_PREFIX_PATH="${srcdir}/tmp_install/usr/lib/cmake/${pkgname}" cmake \
    -S ${pkgname}-${pkgver}/cpp/test \
    -B build_test
  cmake --build build_test
  ctest --test-dir build_test

  CMAKE_PREFIX_PATH="${srcdir}/tmp_install/usr/lib/cmake/${pkgname}" cmake \
    -S ${pkgname}-${pkgver}/cpp/demo \
    -B build_demo
  cmake --build build_demo
  ctest -E "(demo_biharmonic_mpi_*|demo_poisson_mpi_*|demo_hyperelasticity_mpi_*|demo_codim_0_assembly_mpi_*|demo_custom_kernel_mpi_*|demo_poisson_matrix_free_mpi_*|demo_interpolation-io_mpi_*|demo_interpolation_different_meshes_mpi_*)" --test-dir build_demo
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -d ${pkgdir}/usr/share/doc/${pkgname}
  mv ${pkgname}-${pkgver}/cpp/demo ${pkgdir}/usr/share/${pkgname}
  mv ${pkgname}-${pkgver}/cpp/doc/html ${pkgdir}/usr/share/doc/${pkgname}
  install ${pkgname}-${pkgver}/cpp/doc/latex/*.pdf ${pkgdir}/usr/share/doc/${pkgname}
  install -Dm 644 ${pkgname}-${pkgver}/COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
