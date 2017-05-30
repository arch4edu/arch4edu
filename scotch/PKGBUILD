# Maintainer: Samuel Williams <ioquatix>
 
pkgname=scotch
pkgver=6.0.4
_downloadnum=34618  # gforge is insane
pkgrel=3
pkgdesc="Software package and libraries for graph, mesh and hypergraph partitioning, static mapping, and sparse matrix block ordering. This is the all-inclusive version (MPI/serial/esmumps)."
url="http://www.labri.fr/perso/pelegrin/scotch/"
license=("custom:CeCILL-C")
depends=('zlib' 'openmpi' 'bzip2')
provides=('ptscotch' 'ptscotch-openmpi' 'scotch_esmumps' 'scotch_ptesmumps')
conflicts=('ptscotch-openmpi' 'scotch_esmumps' 'scotch_esmumps5')
arch=('i686' 'x86_64')
source=("http://gforge.inria.fr/frs/download.php/file/${_downloadnum}/${pkgname}_${pkgver}.tar.gz")
sha256sums=('f53f4d71a8345ba15e2dd4e102a35fd83915abf50ea73e1bf6efe1bc2b4220c7')
 
prepare() {
  cd "${srcdir}/${pkgname}_${pkgver}/src"

  # Apply patch to fix shared library ldflags
  sed -i 's/$(AR) $(ARFLAGS) $(@) $(?)/$(AR) $(ARFLAGS) $(@) $(?) $(LDFLAGS)/g' libscotch/Makefile
 
  [ -e Makefile.inc ] && rm Makefile.inc
  cp "Make.inc/Makefile.inc.${CARCH/_/-}_pc_linux2.shlib" Makefile.inc
 
  # Use the CFLAGS defined /etc/makepkg.conf
  sed -i "s/-O3/${CFLAGS} -fPIC/g" Makefile.inc
 
  # Fix C compiler
  sed -i "s/CCD\t.*=.*gcc/CCD = mpicc/" Makefile.inc

  # Fix bison/flex
  sed -i "s/define yywrap/define scotchyywrap/" libscotch/parser_ll.l

  # Also enable bzip2 compression
  sed -i "s/-DCOMMON_FILE_COMPRESS_GZ/-DCOMMON_FILE_COMPRESS_GZ -DCOMMON_FILE_COMPRESS_BZ2/" Makefile.inc
  sed -i "s/-lz/-lz -lbz2/" Makefile.inc
 
  # Fix the creation of directories
  sed -i "s/mkdir/mkdir\ -p/" Makefile.inc
 
  # To install headers and libs also for esmumps
  sed -i 's/scotch\*/{scotch,esmumps}\*/g' Makefile
}
 
build() {
  cd "${srcdir}/${pkgname}_${pkgver}/src"
 
  make scotch
  make -j1 esmumps

  # MPI implementation is not thread-safe: compile the parallel versions without SCOTCH_PTHREAD
  sed -i "s/-DSCOTCH_PTHREAD//" Makefile.inc

  make ptscotch
  make -j1 ptesmumps
}
 
check() {
  cd "${srcdir}/${pkgname}_${pkgver}/src"
 
  make check LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:../../lib"
  make ptcheck LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:../../lib"
}
 
package() {
  cd "${srcdir}/${pkgname}_${pkgver}/src"
 
  make install prefix="${pkgdir}/usr" includedir="${pkgdir}/usr/include/scotch"
 
  # To avoid conflict with extra/gpart, maybe move the package to /opt/scotch ?
  mv "${pkgdir}/usr/bin/gpart" "${pkgdir}/usr/bin/gpart-scotch"
 
  install -m 644 -D "${srcdir}/scotch_${pkgver}/doc/CeCILL-C_V1-en.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
