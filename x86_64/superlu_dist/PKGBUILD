# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Gianluca Pettinello <g_pet at hotmail dot com>
# Contributor: Christian Pfeiffer <cpfeiffer at live dot de>
pkgname=superlu_dist
pkgver=8.1.2
pkgrel=2
pkgdesc="Distributed memory, MPI based SuperLU"
arch=('x86_64')
url="https://github.com/xiaoyeli/${pkgname}"
license=('custom')
depends=(lapack parmetis) # openblas combblas
makedepends=(cmake)       # gcc-fortran ninja
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  get_metis_dist.patch::${url}/commit/b64fe36742f1468075670129ac460915eb7130fe.patch)
sha512sums=('30dbd8dbf7a2d86c0b8fdadf6f476473514a8698b15fbdb63e1f2de0d47abd5e1de25f5757ed40c941b4165ae3c53d1132caa8b5a03eaaeea7a4868d13778bf3'
  '4f99d5900917a428597ff788205bd536cb1b591fdf400ed4d9ba0bc05d19f6db7612bd2797d94cdf4572b213758b2e8e7c11919f88023114a4b61d7455d58d9f')
options=('staticlibs')

# -DTPL_ENABLE_COMBBLASLIB=ON \
# -DTPL_COMBBLAS_INCLUDE_DIRS="/usr/include/CombBLAS;/usr/include/CombBLAS/Applications/BipartiteMatchings" \
# -DTPL_COMBBLAS_LIBRARIES="/usr/lib/libCombBLAS.so" \
# -DCMAKE_Fortran_COMPILER=mpifort \

prepare() {
  cd ${pkgname}-${pkgver}
  # https://github.com/xiaoyeli/superlu_dist/issues/141#issuecomment-1519344163
  patch -p1 -i ../get_metis_dist.patch
}

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -Denable_examples=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_CXX_STANDARD=14 \
    -DCMAKE_C_COMPILER=mpicc \
    -DCMAKE_CXX_COMPILER=mpicxx \
    -DXSDK_ENABLE_Fortran=OFF \
    -Denable_doc=OFF \
    -Denable_single=ON \
    -Denable_double=ON \
    -DTPL_PARMETIS_INCLUDE_DIRS="/usr/include" \
    -DTPL_PARMETIS_LIBRARIES="/usr/lib/libparmetis.so" \
    -DTPL_BLAS_LIBRARIES="/usr/lib/libblas.so" \
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
}
