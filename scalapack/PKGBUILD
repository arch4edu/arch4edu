# Contributor: Myles English <myles at rockhead dot biz>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=scalapack
pkgver=2.1.0
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc="subset of scalable LAPACK routines redesigned for distributed memory MIMD parallel computers."
url="http://www.netlib.org/scalapack/"
license=('custom')
depends=('glibc' 'openmpi' 'blas' 'lapack') # 'atlas-lapack' 'blacs-openmpi' )
makedepends=('cmake' 'gcc-fortran')
provides=('blacs')
install=${pkgname}.install
source=(http://www.netlib.org/scalapack/$pkgname-$pkgver.tgz http://www.netlib.org/scalapack/manpages.tgz Makefile example1.f)
sha256sums=('61d9216cf81d246944720cfce96255878a3f85dec13b9351f1fa0fd6768220a6'
            'a745c9f367d65e3c7611c126597a4681094b002552e47b621964d30a966aac7b'
            '5f7e81c1c76fc010677fd446bfc689c7f6af1a22a51093e8790e8a615159c541'
            'd9904ecb69f318c4782c0bd39ff2bff511af31960a2383a9d42d6620a266ea70')

prepare() {
  cd ${pkgname}-${pkgver}
  sed -i 's/MPI_Type_struct/MPI_Type_create_struct/g' BLACS/SRC/*.c
  sed -i 's/MPI_Attr_get/MPI_Comm_get_attr/g' BLACS/SRC/blacs_get_.c
}

build() {
    msg "Starting make..."

    [[ -e build ]] && rm -rf build
    mkdir build 
    cd build

    cmake ../${pkgname}-${pkgver} \
	-DCMAKE_INSTALL_PREFIX="${pkgdir}"/usr \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_CXX_COMPILER=/usr/bin/mpic++ \
	-DCMAKE_C_COMPILER=/usr/bin/mpicc
    make
}

package(){
  cd "${srcdir}"/build
  make install #DESTDIR="${pkgdir}"

  sed -i 's#'${pkgdir}'##g' "${pkgdir}"/usr/lib/pkgconfig/scalapack.pc

  # Install headers
  install -m 755 -d "${pkgdir}"/usr/include
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/PBLAS/SRC/*.h "${pkgdir}"/usr/include
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/BLACS/SRC/*.h "${pkgdir}"/usr/include

  # Install man pages
  install -m 755 -d "${pkgdir}"/usr/share/man/manl
  install -m 644 "${srcdir}"/MANPAGES/man/manl/*.l ${PREFIX} "${pkgdir}"/usr/share/man/manl

  # Install test
  install -m 755 -d "${pkgdir}"/usr/share/$pkgname/testing
  install -m 755 "${srcdir}"/build/TESTING/x* "${pkgdir}"/usr/share/$pkgname/testing
  install -m 644 "${srcdir}"/build/TESTING/*.dat "${pkgdir}"/usr/share/$pkgname/testing

  # Install examples
  install -m 755 -d "${pkgdir}"/usr/share/$pkgname/examples
  install -m 644 "${srcdir}"/Makefile "${pkgdir}"/usr/share/${pkgname}/examples
  install -m 644 "${srcdir}"/example1.f "${pkgdir}"/usr/share/${pkgname}/examples

  # Install license
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/LICENSE \
	  "${pkgdir}"/usr/share/licenses/$pkgname/LICENSE
}
