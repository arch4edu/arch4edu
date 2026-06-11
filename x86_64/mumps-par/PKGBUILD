# Maintainer: Michele Mocciola <mickele>
# Contributor: Guillaume Dollé < dolle dot guillaume at gmail dot com >
# Contributor: Lucas H. Gabrielli
pkgname=mumps-par
pkgver=5.9.0
pkgrel=1
pkgdesc="Sparse solver library using Gaussian elimination, with parmetis implementation"
url="https://mumps-solver.org/index.php"
license=("custom")
depends=('lapack' 'openmpi' 'scotch' 'scalapack' 'parmetis' 'metis' 'zlib' 'bzip2')
makedepends=('gcc-fortran')
provides=('mumps')
conflicts=('mumps')
arch=('i686' 'x86_64')
source=(https://mumps-solver.org/MUMPS_${pkgver}.tar.gz
        Makefile.inc)
sha256sums=('02c6efdb91749ec0f82351d40f3f860547272a1eb1d899126a4265b4d6bcc4ca'
            'e908b95991d58c155d48c1058447587a030b0bd6afa7de5905c88393f45d8b68')

prepare() {
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
  install -m 755 -d "${pkgdir}/usr/include"
  install -D -m644 *.h "${pkgdir}/usr/include"

  # Install all libraries
  cd "${srcdir}/MUMPS_${pkgver}/lib"
  install -m 755 -d "${pkgdir}/usr/lib"
  install -D -m644 lib* ${pkgdir}/usr/lib

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
  install -m 644 "${srcdir}/MUMPS_${pkgver}/Makefile.inc" "${pkgdir}/usr/share/doc/${pkgname}/examples"
  sed -i 's_\(topdir =\).*_\1 /usr_g; s-.*\(Makefile.inc\)-include Makefile.inc-g' "${pkgdir}/usr/share/doc/${pkgname}/examples/Makefile"

  # Install license
  install -D -m644 "${srcdir}/MUMPS_${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
