# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Myles English <myles at rockhead dot biz>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=scalapack
pkgver=2.2.0
pkgrel=2
arch=('i686' 'x86_64')
pkgdesc="subset of scalable LAPACK routines redesigned for distributed memory MIMD parallel computers."
url="http://www.netlib.org/scalapack/"
license=('custom')
depends=('glibc' 'openmpi' 'blas' 'lapack') # 'atlas-lapack' 'blacs-openmpi' )
makedepends=('cmake' 'gcc-fortran')
provides=('blacs')
install=${pkgname}.install
source=(http://www.netlib.org/scalapack/$pkgname-$pkgver.tgz http://www.netlib.org/scalapack/manpages.tgz Makefile example1.f)
sha512sums=('1e6c69a4faab8165c273479ff8b63e98df6a7253cffc524b5700d0344c3f89c52c5bccc5d3a9a9bded4d9da50080123abd8340b75e1f92317e471c4375704999'
            '471e77c441219aa7d00a1210bc0db9deb23a0187a43575fb7a975df180669fee5a8282e102789ac4e5aeb73e2a330a29a548c4e379f611b29ee6369757381166'
            '860b30a63f8e7a0d8a567efe035256f52ff1bb8edb6612221503d870de83e12daf904334f3915c01c8cf8b780bc8f1b93dd86be52bd1eeb7d743b1d8053bbcaf'
            '0a71ba337f6515c71e640e973bf16b7125310b1711827ccbf8e38374e2b5f8b2650b6b56285fea3fb9587f0003f1a86aa23b0c078a8bb00605549f5192ca3f64')


build() {
  cmake -S ${pkgname}-${pkgver} \
        -B build \
        -D CMAKE_INSTALL_PREFIX:PATH=/usr \
        -D BUILD_SHARED_LIBS:BOOL=ON \
        -D SCALAPACK_BUILD_TESTS:BOOL=OFF \
        -D CMAKE_BUILD_TYPE:STRING=Release \
        -D CMAKE_Fortran_FLAGS:STRING="$FCFLAGS -fallow-argument-mismatch"
  make -C build
}

package(){
  DESTDIR=${pkgdir} cmake --install build

  # Install headers
  install -m 755 -d "${pkgdir}"/usr/include
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/PBLAS/SRC/*.h "${pkgdir}"/usr/include
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/BLACS/SRC/*.h "${pkgdir}"/usr/include

  # Install man pages
  install -m 755 -d "${pkgdir}"/usr/share/man/manl
  install -m 644 "${srcdir}"/MANPAGES/man/manl/*.l ${PREFIX} "${pkgdir}"/usr/share/man/manl

  # Install examples
  install -m 755 -d "${pkgdir}"/usr/share/$pkgname/examples
  install -m 644 "${srcdir}"/Makefile "${pkgdir}"/usr/share/${pkgname}/examples
  install -m 644 "${srcdir}"/example1.f "${pkgdir}"/usr/share/${pkgname}/examples

  # Install license
  install -m 644 -D "${srcdir}"/${pkgname}-${pkgver}/LICENSE \
	  "${pkgdir}"/usr/share/licenses/$pkgname/LICENSE
}
