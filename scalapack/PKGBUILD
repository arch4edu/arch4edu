# Contributor: Myles English <myles at rockhead dot biz>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=scalapack
pkgver=2.0.2
pkgrel=5
pkgdesc="subset of scalable LAPACK routines redesigned for distributed memory MIMD parallel computers."
url="http://www.netlib.org/scalapack/"
license=('custom')
depends=('glibc' 'openmpi' 'blas' 'lapack') # 'atlas-lapack' 'blacs-openmpi' )
makedepends=('cmake' 'gcc-fortran')
provides=('blacs')
conflicts=()
replaces=()
backup=()
arch=('i686' 'x86_64')
install=${pkgname}.install
source=(http://www.netlib.org/scalapack/$pkgname-$pkgver.tgz http://www.netlib.org/scalapack/manpages.tgz Makefile example1.f)
md5sums=('2f75e600a2ba155ed9ce974a1c4b536f'
         'a536ab4837ec68addff0a3ec99427a10'
         '0bef36150ffaf341a6228b474ed800c9'
         '4723ad431356431bb193db254b6ee0fb')

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
       # doesn't work (?): -DCMAKE_INSTALL_LOCAL_ONLY=0 \
       #-DCMAKE_CXX_FLAGS='fPIC' CMAKE_Fortran_FLAGS

    make

  # Builds library, test and example
  # make lib
  #   ld -Bshareable -o  "${srcdir}"/${pkgname}-${pkgver}/lib${pkgname}.so -x -soname lib${pkgname}.so --whole-archive $startdir/src/${pkgname}-${pkgver}/lib${pkgname}.a
  #   make exe
  #   make example
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
