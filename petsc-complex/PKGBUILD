# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Sigvald Marholm <marholm@marebakken.com>
# Adapted from the package petsc with the following original contributors:
# Contributor: Martin Diehl <https://martin-diehl.net>
# Contributor: Andreas Bilke <abilke at cosy dot sbg dot ac dot at>
# Contributor: Myles English <myles at rockhead dot biz>
# Contributor: Lucas H. Gabrielli <heitzmann at gmail dot com>

pkgname=petsc-complex
_pkgname=petsc
pkgver=3.15.0
pkgrel=1
_config=linux-c-opt
# if --with-debugging=yes is set then PETSC_ARCH is automatically set to
#"linux-c-debug" for some things, so the _config should be changed too
#_config=linux-c-debug
pkgdesc="Portable, extensible toolkit for scientific computation (complex scalars)"
arch=('x86_64')
url="https://www.mcs.anl.gov/petsc/"
license=('BSD')
options=(staticlibs)
conflicts=('petsc')
provides=('petsc')
depends=(
  'boost'
  'tcsh'
  'fftw'
  'hdf5-openmpi'
  'hypre'
  'lapack'
  'openmpi'
  'python'
  'suitesparse'
  'triangle'
)
_depends=(
  'metis'
  'mumps'
  'parmetis'
  'pastix'
  'scotch'
  'superlu'
  'superlu_dist'
)
makedepends=(${_depends[@]} 'cmake' 'gcc-fortran')
optdepends=(${_depends[@]} 'trilinos')
install=petsc.install
source=(http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/${_pkgname}-lite-${pkgver/_/-}.tar.gz
        test_optdepends.sh)
sha256sums=('ac46db6bfcaaec8cd28335231076815bd5438f401a4a05e33736b4f9ff12e59a'
            '902f8d222706868184cfeff94b1c26a781fd9553a43a66deac7cc1317de82a86')

_install_dir=/opt/petsc/${_config}
_petsc_arch="arch-${_config}"

build() {
  _build_dir="${srcdir}/${_pkgname}-${pkgver/_/-}"

  cd ${_build_dir}

  unset PETSC_ARCH
  export PETSC_DIR=${_build_dir}

  CONFOPTS="--with-shared-libraries=1 --COPTFLAGS=-O3 --CXXOPTFLAGS=-O3 --FOPTFLAGS=-O3 \
            --with-cc=$(which mpicc) --with-cxx=$(which mpicxx) --with-fc=$(which mpifort) \
            --with-scalar-type=complex"
  CONFOPTS="${CONFOPTS} $(sh ${srcdir}/test_optdepends.sh)"

  echo ${CONFOPTS}
  python ./configure \
    --prefix=${_install_dir} \
    --PETSC_ARCH=${_petsc_arch} \
    ${CONFOPTS}

  make ${MAKEFLAGS} PETSC_DIR=${_build_dir} PETSC_ARCH=${_petsc_arch} all
}

check() {
  _build_dir="${srcdir}/${_pkgname}-${pkgver/_/-}"
  cd ${_build_dir}

  make check
}

package() {
  _build_dir="${srcdir}/${_pkgname}-${pkgver/_/-}"

  cd ${_build_dir}
  echo "make ${MAKEFLAGS} PETSC_DIR=${_build_dir} DESTDIR=${pkgdir} install"
  export PETSC_DIR=${_build_dir}
  make ${MAKEFLAGS} PETSC_DIR=${_build_dir} DESTDIR=${pkgdir} install

  rm -rf ${pkgdir}/opt/petsc/linux-c-opt/lib/petsc/bin/__pycache__

  export PETSC_DIR=${_install_dir}

  # install licence (even though there is no such word as licenses)
  install -Dm 644 ${_build_dir}/LICENSE ${pkgdir}/usr/share/licenses/$pkgname/LICENSE

  mkdir -p ${pkgdir}/etc/profile.d
  echo "export PETSC_DIR=${_install_dir}" > ${pkgdir}/etc/profile.d/petsc.sh
  chmod +x ${pkgdir}/etc/profile.d/petsc.sh

  # show where the shared libraries are
  install -dm 755 "${pkgdir}"/etc/ld.so.conf.d/
  echo "${_install_dir}/lib" > "${pkgdir}"/etc/ld.so.conf.d/petsc.conf

  # install pkgconfig settings
  install -Dm 644 "${_build_dir}/${_petsc_arch}"/lib/pkgconfig/PETSc.pc "${pkgdir}"/usr/share/pkgconfig/PETSc.pc
}
