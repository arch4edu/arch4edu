# Maintainer: Giuseppe Borzi <gborzi___AT___ieee___DOT___org>
# Contributor: mickele <mimocciola___AT___yahoo___DOT___ com>
# Contributor: iztok pizorn <pizorn___AT___gmail___DOT___com>
# Contributor: olivier medoc <o_medoc___AT___yahoo___DOT___fr>
pkgname=atlas-lapack
pkgver=3.10.3
_lapackver=3.6.1
pkgrel=1
pkgdesc="Complete LAPACK and BLAS implementation using optimised ATLAS routines"
url="http://math-atlas.sourceforge.net/"
depends=('gcc-libs')
makedepends=('binutils' 'sed' 'gcc-fortran')
arch=('i686' 'x86_64')
conflicts=('blas' 'lapack' 'cblas' 'atlas-lapack-base')
provides=("blas" "lapack=$_lapackver" 'cblas' 'atlas-lapack-base')
license=('custom:blas' 'custom:lapack' 'custom:atlas')
options=(!makeflags)
install=$pkgname.install
source=(http://www.netlib.org/lapack/lapack-$_lapackver.tgz
        http://downloads.sourceforge.net/math-atlas/atlas${pkgver}.tar.bz2
        blas-license.txt atlas-license.txt
        makefile.shared.mt makefile.shared.st)
noextract=(lapack-$_lapackver.tgz atlas$pkgver.tar.bz2)
md5sums=('421b2cb72e15f237e144428f9c460ee0'
         'd6ce4f16c2ad301837cfb3dade2f7cef'
         '38b6acb8ed5691d25863319d30a8b365'
         '4903eb06072dfbf94710691ccb6660bf'
         'e293bf3b62b7cc02cb5dcf54f9f40053'
         '5153cb945e8f386e4d98d4b0fe791776')

build() {
   msg 'Before building this package, as root you must set the CPU(s)'
   msg 'governor(s) to "performance".'
   msg 'See: https://wiki.archlinux.org/index.php/CPU_frequency_scaling'

   cd "$srcdir"
   tar -xjf atlas$pkgver.tar.bz2

   unset MAKE
   CORE=`cat /proc/cpuinfo | grep "cpu MHz" | head -n 1 | sed "s/.*: \([0-9.]*\).*/\1/"`
   NCPU=`grep "^processor" /proc/cpuinfo | wc -l`
   if [ "$CARCH" = "x86_64" ]; then
      ARCHITECTURE_BUILD_OPTS="-b 64" # for x86_64
   else
      ARCHITECTURE_BUILD_OPTS="-b 32" # for i686
   fi

   cd "$srcdir"/ATLAS
   rm -rf build
   mkdir -p build
   cd build

   msg 'Configuring ATLAS'

   ../configure --prefix=/usr/ $ARCHITECTURE_BUILD_OPTS -Fa alg -fPIC \
      --shared -D c -DPentiumCPS=$CORE \
      --with-netlib-lapack-tarfile="$srcdir/lapack-$_lapackver.tgz"

   msg 'Building ATLAS'

   make build

   msg 'Building shared libraries'
   cd lib
   if [ 1 -lt $NCPU ]; then
      cp "$srcdir/makefile.shared.mt" makefile
   else
      cp "$srcdir/makefile.shared.st" makefile
   fi
   make -f makefile
}

check() {
   cd "$srcdir/ATLAS/build"
   unset MAKE

   msg 'Checking ATLAS'

   make check
   make ptcheck
   make time
}

package() {
   cd "$srcdir/ATLAS/build"
   unset MAKE

   msg 'Packaging ATLAS'

   make DESTDIR="$pkgdir/usr" install
   cp -d lib/*.so* "$pkgdir/usr/lib"
   [ -e lib/libptlapack.a ] && cp lib/libptlapack.a "$pkgdir/usr/lib"
   cd "$pkgdir/usr/lib"
   ln -s libblas.so libblas.so.3
   ln -s liblapack.so.3 liblapack.so

   install -Dm644 "${srcdir}/blas-license.txt" \
      "${pkgdir}/usr/share/licenses/$pkgname/blas-license.txt"
   install -Dm644 "${srcdir}/ATLAS/build/src/lapack/reference/LICENSE" \
      "${pkgdir}/usr/share/licenses/$pkgname/lapack-license.txt"
   install -Dm644 "${srcdir}/atlas-license.txt" \
      "${pkgdir}/usr/share/licenses/$pkgname/atlas-license.txt"
}

