# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Myles English <myles at rockhead dot biz>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=scalapack
pkgver=2.2.2
pkgrel=2
pkgdesc='Subset of scalable LAPACK routines redesigned for distributed memory computers'
arch=(i686 x86_64 aarch64)
url=http://www.netlib.org/scalapack
license=(BSD-3-Clause)
depends=(glibc openmpi blas lapack)
makedepends=(cmake gcc-fortran)
provides=(blacs)
#source=(https://github.com/Reference-ScaLAPACK/scalapack/archive/scalapack_$pkgver/$pkgname-$pkgver.tar.gz)
source=(https://github.com/Reference-ScaLAPACK/scalapack/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('1b91b94a081cd808dc6fa7d23a9f4054f4d23de293cae1686f7708237c28404561a6f4185e7f27a0a56cd0916622f8db444803f8ed19d56368af54a44c455d44')

build() {
  cmake -S ${pkgname}-${pkgver} \
        -B build \
        -D CMAKE_INSTALL_PREFIX:PATH=/usr \
        -D BUILD_SHARED_LIBS:BOOL=ON \
        -D SCALAPACK_BUILD_TESTS:BOOL=OFF \
        -D CMAKE_BUILD_TYPE:STRING=Release \
        -D CMAKE_Fortran_FLAGS:STRING="$FCFLAGS -fallow-argument-mismatch" \
        -D CMAKE_C_FLAGS:STRING="$CFLAGS -Wno-implicit-function-declaration" \
        -D CMAKE_C_STANDARD:STRING="17"
  make -C build
}

prepare() {
  sed -i 's/cmake_minimum_required(VERSION 2.8)/cmake_minimum_required(VERSION 3.6)/g' ${pkgname}-${pkgver}/BLACS/INSTALL/CMakeLists.txt
}

package(){
  DESTDIR="${pkgdir}" cmake --install build

  # Install headers
  install -m 755 -d "${pkgdir}"/usr/include
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/PBLAS/SRC/*.h "${pkgdir}"/usr/include
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/BLACS/SRC/*.h "${pkgdir}"/usr/include

  # Install license
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/LICENSE \
	  "${pkgdir}"/usr/share/licenses/$pkgname/LICENSE
}
