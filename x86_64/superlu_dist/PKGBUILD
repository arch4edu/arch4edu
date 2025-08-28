# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Auto update bot <auto-update-bot@arch4edu.org>
# Maintainer: Gianluca Pettinello <g_pet at hotmail dot com>
# Contributor: Christian Pfeiffer <cpfeiffer at live dot de>
pkgname=superlu_dist
pkgver=9.1.0
pkgrel=2
pkgdesc="Distributed memory, MPI based SuperLU"
arch=(x86_64)
url="https://github.com/xiaoyeli/${pkgname}"
license=(LicenseRef-Callaway-BSD)
depends=(lapack parmetis-git python-mpi4py) # openblas combblas
makedepends=(cmake gcc-fortran)             # ninja
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('76251ac49ff03ca9b040a9ce34764047fe182f1361d05e5e73b6df92510135170c9c946d15d716dadc3326995515a703b999a56bd762e6f77e9b8749f298fed1')
options=('staticlibs')

# -DTPL_ENABLE_COMBBLASLIB=ON \
# -DTPL_COMBBLAS_INCLUDE_DIRS="/usr/include/CombBLAS;/usr/include/CombBLAS/Applications/BipartiteMatchings" \
# -DTPL_COMBBLAS_LIBRARIES="/usr/lib/libCombBLAS.so" \

prepare() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  # https://github.com/xiaoyeli/superlu_dist/pull/185
  sed -i -e 's/\*fp, \*fopen()/\*fp/g' -e 's/\*fopen(), //g'  $(find -name '*.c')
}

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_STANDARD=11 \
    -DCMAKE_C_COMPILER=mpicc \
    -DCMAKE_CXX_COMPILER=mpicxx \
    -DCMAKE_Fortran_COMPILER=mpifort \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=None \
    -DBUILD_STATIC_LIBS=TRUE \
    -DBUILD_TESTING=OFF \
    -DXSDK_ENABLE_Fortran=ON \
    -Denable_complex16=ON \
    -Denable_doc=OFF \
    -Denable_double=ON \
    -Denable_examples=OFF \
    -Denable_python=ON \
    -Denable_single=ON \
    -Denable_tests=ON \
    -DTPL_BLAS_LIBRARIES="/usr/lib/libblas.so" \
    -DTPL_PARMETIS_INCLUDE_DIRS="/usr/include" \
    -DTPL_PARMETIS_LIBRARIES="/usr/lib/libparmetis.so" \
    -DTPL_LAPACK_LIBRARIES="/usr/lib/liblapack.so" \
    -DTPL_ENABLE_LAPACKLIB=ON \
    -DTPL_ENABLE_PARMETISLIB=ON \
    -DTPL_ENABLE_COMBBLASLIB=OFF \
    -DTPL_ENABLE_CUDALIB=OFF \
    -DTPL_ENABLE_HIPLIB=OFF \
    -DTPL_ENABLE_INTERNAL_BLASLIB=OFF \
    -DCMAKE_INSTALL_INCLUDEDIR=include/superlu_dist \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm644 ${pkgname}-${pkgver}/README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
  install -Dm644 ${pkgname}-${pkgver}/License.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 ${pkgname}-${pkgver}/DOC/ug.pdf "${pkgdir}/usr/share/doc/${pkgname}/ug.pdf"

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  install -d ${pkgdir}${site_packages}
  mv ${pkgdir}/usr/lib/PYTHON/ ${pkgdir}${site_packages}/${pkgname}
  rm -r ${pkgdir}/usr/include/${pkgname}/FORTRAN
}
