# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: eDgar <eDgar |at| openmail.cc >
# Contributor: Michele Mocciola <mickele>
# Contributor: Guillaume Dollé < dolle dot guillaume at gmail dot com >
# Contributor: Lucas H. Gabrielli
pkgname=mumps
pkgver=5.8.2
pkgrel=1
pkgdesc='Sparse solver library using Gaussian elimination'
url='https://mumps-solver.org'
license=('custom')
depends=('lapack' 'openmpi' 'scotch' 'scalapack' 'metis' 'zlib' 'bzip2')
makedepends=('gcc-fortran')
conflicts=('mumps-par' 'mumps4')
arch=('i686' 'x86_64')
source=(https://mumps-solver.org/MUMPS_${pkgver}.tar.gz
        Makefile.inc)
sha512sums=('1dcb609194400ad85f403fd09d9ee2ff5979161232b36e075ae0fac4eabc651a9277721a3b7672e3e3b5f2020aad13b920376f1e93bf403891f75c0c385b061a'
            '348dc692cb66f428d38808e4ec50c259a7a841d6c09ccd9fce829a731967358e7b9db2be5436b86e20539ddcc014b7c577fb5dd0d114a418a91573f49cf38ef0')

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
  MPIRUN="mpirun -np 3 --mca plm_rsh_agent sh --mca opal_warn_on_missing_libcuda 0 --oversubscribe"
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
