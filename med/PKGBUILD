# Maintainer Oliver Goethel <deezy>
# Contributor: Michele Mocciola <mickele>
# Contributor: Brice Méalier <mealier_brice@yahoo.fr>
# Contributor: Philippe Miron <tuxication@gmail.com>
# Modified by: César Vecchio <cesar UNDERSTRIKE vecchio AT yahoo DOT com>
# Modified by: Martin Ortbauer <mortbauer@gmail.com>
     
pkgname=med
pkgver=3.2.0
pkgrel=5
pkgdesc="MED stands for Modelisation et Echanges de Donnees, i.e. Data Modelization and Exchanges - MED is code-aster exchange module linked to hdf5"
url="http://www.code-aster.org/outils/med/"
license=('LGPL')
depends=('hdf5' 'openmpi' 'swig')
makedepends=('gcc-fortran' 'coreutils' 'python2')
optdepends=('tk')
provides=()
conflicts=('med_fichier')
replaces=('med_fichier')
backup=()
arch=('i686' 'x86_64')
source=("http://files.salome-platform.org/Salome/other/${pkgname}-${pkgver}.tar.gz"
        "patch-include_2.3.6_med.h.in"
        "patch-include_med.h.in"
        "patch-src_2.3.6_ci_MEDequivInfo.c"
        "patch-int2long")
md5sums=('eb61df92f0624feb6328f517cd756a23'
         'b83949326d7ae0ca77a06822b754a329'
         '14a151cea108388d7a3b4c62887169f6'
         '8f0cbf6f08783a6ba68ff5ab240dd62e'
         'be65d145b85ed5b19a709d9dee84b6d2')
 
build() {
  if [ "$CARCH" = "x86_64" ]; then
    export FFLAGS="-fopenmp -fPIC -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -ffixed-line-length-0 ${CFLAGS}"
    export FCFLAGS="-fopenmp -fPIC -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -ffixed-line-length-0 ${CFLAGS}"
    export CPPFLAGS="-DHAVE_F77INT64 ${CPPFLAGS}"
    export F77=mpif90
    export FC=mpif90
  else # i686
    export FFLAGS="-fopenmp -fPIC -ffixed-line-length-0 ${CFLAGS}"
    export FCFLAGS="-fopenmp -fPIC -ffixed-line-length-0 ${CFLAGS}"
    export F77=mpif90
    export FC=mpif90
  fi
  
  export PYTHON="$(which python2)"

  cd ${srcdir}/${pkgname}-${pkgver} || return 1
 
  # patch H5public_extract.h.in
  sed -i -e '/^#typedef/ s/#/\/\//' ./include/H5public_extract.h.in
  
  #patch for hdf5-1.10
  patch -p0 < ${srcdir}/patch-include_2.3.6_med.h.in
  patch -p0 < ${srcdir}/patch-include_med.h.in
  patch -p0 < ${srcdir}/patch-src_2.3.6_ci_MEDequivInfo.c
  patch -p0 < ${srcdir}/patch-int2long
 
  ./configure --with-f90=mpif90 --prefix=/usr --datadir=/usr/share/med --with-swig=yes || return 1
  make || return 1
}
 
package() {
  cd ${srcdir}/${pkgname}-${pkgver} || return 1
 
  make DESTDIR=${pkgdir} install || return 1
  # now move the testprograms to share, we don't want all the stuff in the bindir
  cp -dpr --no-preserve=ownership ${pkgdir}/usr/bin/testc ${pkgdir}/usr/share/med/testc
  cp -dpr --no-preserve=ownership ${pkgdir}/usr/bin/testf ${pkgdir}/usr/share/med/
  cp -dpr --no-preserve=ownership ${pkgdir}/usr/bin/unittests ${pkgdir}/usr/share/med/
  cp -dpr --no-preserve=ownership ${pkgdir}/usr/bin/usescases ${pkgdir}/usr/share/med/
  rm -r ${pkgdir}/usr/bin/{usescases,unittests,testf,testc}
}

