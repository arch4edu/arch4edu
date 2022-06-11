# Maintainer: Michele Mocciola <mickele>
# Contributor: Guillaume Dollé < dolle dot guillaume at gmail dot com >
# Contributor: Lucas H. Gabrielli
pkgname=mumps-par
pkgver=5.3.1
pkgrel=3
pkgdesc="Sparse solver library using Gaussian elimination, with parmetis implementation"
url="http://mumps.enseeiht.fr"
license=("custom")
depends=('lapack' 'openmpi' 'scotch>=6.0.3-3' 'scalapack' 'parmetis' 'metis' 'zlib' 'bzip2')
makedepends=('gcc-fortran')
provides=('mumps')
conflicts=('mumps')
backup=()
arch=('i686' 'x86_64')
source=(http://mumps.enseeiht.fr/MUMPS_${pkgver}.tar.gz
        Makefile.inc
        MUMPS-shared.patch
        MUMPS-shared-pord.patch
        MUMPS-shared-seq.patch)
sha256sums=('774fc9411a3ab4704bc907cb7d30090ce6a65b83cde32549c58d3e9f63594e1a'
            'b5d3baf74f14f30f7888cc6847ffdf43184aaa9609dd21b9d9ab94a9070639ee'
            '51c754c0d34b461f3635ce2731f82e9c51d512528caf72cac5041380259d063d'
            'e47d0bb48d278c96963bf0de2a6282836fef80af4344376c2a796c59c723053f'
            '6ae456e4969d1af5ce8f209932d65f2d2dbe475a1fa99c303a6eb92d6771788f')

build() {
  cd "${srcdir}/MUMPS_${pkgver}"
  cp "${srcdir}/Makefile.inc" .
  patch -Np0 < ../MUMPS-shared.patch
  patch -Np0 < ../MUMPS-shared-pord.patch
  patch -Np0 < ../MUMPS-shared-seq.patch
  
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${srcdir}/MUMPS_${pkgver}/lib
  SONAME_VERSION=$pkgver make -j1 alllib || return 1
}

package(){
  # Install all headers
  cd "${srcdir}/MUMPS_${pkgver}/include"
  install -m 755 -d "${pkgdir}/usr/include"
  install -D -m644 *.h "${pkgdir}/usr/include"

  # Install all libraries
  cd "${srcdir}/MUMPS_${pkgver}/lib" || return 1
  install -m 755 -d "${pkgdir}/usr/lib" || return 1
  install -D -m644 lib* ${pkgdir}/usr/lib || return 1

  # Install libraries mpiseq
  cd "${srcdir}/MUMPS_${pkgver}/libseq"
  install -m 755 -d "${pkgdir}/usr/include/mpiseq"
  install -D -m644 *.h "${pkgdir}/usr/include/mpiseq"
  cd "${srcdir}/MUMPS_${pkgver}/libseq"
  install -D -m644 lib* ${pkgdir}/usr/lib

  # Install examples
  install -m 755 -d "${pkgdir}/usr/share/doc/${pkgname}/examples"
  cd "${srcdir}/MUMPS_${pkgver}/examples"
  install -m 644 * "${pkgdir}/usr/share/doc/${pkgname}/examples"
  #for _FILE in ssimpletest dsimpletest csimpletest zsimpletest c_example; do
  #  chmod 0755 "${pkgdir}/usr/share/doc/${pkgname}/examples/${_FILE}"
  #done

  # Install license
  install -D -m644 "${srcdir}/MUMPS_${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
