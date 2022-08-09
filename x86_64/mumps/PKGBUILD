# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: eDgar <eDgar |at| openmail.cc >
# Contributor: Michele Mocciola <mickele>
# Contributor: Guillaume Dollé < dolle dot guillaume at gmail dot com >
# Contributor: Lucas H. Gabrielli
pkgname=mumps
pkgver=5.5.1
pkgrel=1
pkgdesc='Sparse solver library using Gaussian elimination'
url='http://mumps.enseeiht.fr'
license=('custom')
depends=('lapack' 'openmpi' 'scotch' 'scalapack' 'metis' 'zlib' 'bzip2')
makedepends=('gcc-fortran')
conflicts=('mumps-par' 'mumps4')
arch=('i686' 'x86_64')
source=(http://graal.ens-lyon.fr/MUMPS/MUMPS_${pkgver}.tar.gz
        Makefile.inc)
sha512sums=('51ebc680ada41f5d622a353778233d6306f78ac25e30a3a5ba181b16961093215d4a2e715727340f6865abd0cf0a90d88665b13ddc36007f76eb8fcbc0ed5adf'
            'bd1d72ab2638b4d28c560c182c5b5bd2c67d269ddcbe27afd7077caad4007fd0475a442710f27edaca293ecaf4ae70e7b2adc1e16e81e683929634c89c30a43f')

prepare () {
  cd "${srcdir}/MUMPS_${pkgver}"
  cp "${srcdir}/Makefile.inc" .
}

build() {
  cd "${srcdir}/MUMPS_${pkgver}"
  make all
}

check () {
  cd "${srcdir}/MUMPS_${pkgver}/examples"
  make all
  # From the README (in examples)
  MPIRUN="mpirun -np 3 --mca opal_warn_on_missing_libcuda 0 --oversubscribe"
  export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${srcdir}/MUMPS_${pkgver}/lib"
  ${MPIRUN} ./ssimpletest < input_simpletest_real
  ${MPIRUN} ./dsimpletest < input_simpletest_real
  ${MPIRUN} ./csimpletest < input_simpletest_cmplx
  ${MPIRUN} ./zsimpletest < input_simpletest_cmplx
  ${MPIRUN} ./c_example
  ${MPIRUN} ./multiple_arithmetics_example
  ${MPIRUN} ./ssimpletest_save_restore < input_simpletest_real
  ${MPIRUN} ./dsimpletest_save_restore < input_simpletest_real
  ${MPIRUN} ./csimpletest_save_restore < input_simpletest_cmplx
  ${MPIRUN} ./zsimpletest_save_restore < input_simpletest_cmplx
  ${MPIRUN} ./c_example_save_restore
}

package(){
  # Install all headers
  cd "${srcdir}/MUMPS_${pkgver}/include"
  install -d -m755 "${pkgdir}/usr/include"
  install -D -m644 *.h "${pkgdir}/usr/include"

  # Install all libraries
  cd "${srcdir}/MUMPS_${pkgver}/lib"
  install -d -m755 ${pkgdir}/usr/lib
  install -D -m644 *.so ${pkgdir}/usr/lib

  # Install examples
  install -m 755 -d "${pkgdir}/usr/share/doc/${pkgname}/examples"
  cd "${srcdir}/MUMPS_${pkgver}/examples"
  install -m 644 * "${pkgdir}/usr/share/doc/${pkgname}/examples"
  install -m 644 "${srcdir}/MUMPS_${pkgver}/Makefile.inc" "${pkgdir}/usr/share/doc/${pkgname}/examples"
  sed -i 's_\(topdir =\).*_\1 /usr_g; s-.*\(Makefile.inc\)-include Makefile.inc-g' "${pkgdir}/usr/share/doc/${pkgname}/examples/Makefile"

  # Install license
  install -D -m644 "${srcdir}/MUMPS_${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
