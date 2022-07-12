# Maintainer: Jonathon Fernyhough <jonathon + m2x + dev>
# Contributor: Sven-Hendrik Haase <svenstaro@gmail.com>
# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: libtool requires rebuilt with each new gcc version

pkgname=(gcc8 gcc8-libs gcc8-fortran)
pkgver=8.5.0
_pkgver=8
_majorver=${pkgver:0:1}
_islver=0.24
pkgrel=2
pkgdesc='The GNU Compiler Collection (8.x.x)'
arch=(x86_64)
license=(GPL LGPL FDL custom)
url='http://gcc.gnu.org'
makedepends=(binutils libmpc doxygen python)
checkdepends=(dejagnu inetutils)
options=(!emptydirs !lto)
_libdir=usr/lib/gcc/$CHOST/${pkgver%%+*}
source=(https://sourceware.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.xz{,.sig}
        https://sourceware.org/pub/gcc/infrastructure/isl-${_islver}.tar.bz2
        c89 c99)
validpgpkeys=(13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              D3A93CAD751C2AF4F8C7AD516C35B99309B5FA62) # Jakub Jelinek <jakub@redhat.com>
sha512sums=('92f599680e6b7fbce88bcdda810f468777d541e5fddfbb287f7977d51093de2a5178bd0e6a08dfe37090ea10a0508a43ccd00220041abbbec33f1179bfc174d8'
            'SKIP'
            'aab3bddbda96b801d0f56d2869f943157aad52a6f6e6a61745edd740234c635c38231af20bc3f1a08d416a5e973a90e18249078ed8e4ae2f1d5de57658738e95'
            'aa3fe5cd3259bc74ed464b4dcccbabe0933628e6f2997d7e9abbfb4fd558dd1f6db79dec55970b9173e49c479e0b87e9d743d8087f3912b256fa78e38e17430d'
            'b3962925604937d49527bf790d15aad2966cca86e419b7f79bff15f971931924af6a57883d8529a72630caac59be1598374793cf152056cda8278f6f6e674834')

prepare() {
  [[ ! -d gcc ]] && ln -s gcc-${pkgver/+/-} gcc
  cd gcc

  # link isl for in-tree build
  ln -s ../isl-${_islver} isl

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  mkdir -p "$srcdir/gcc-build"
}

build() {
  cd gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  CFLAGS=${CFLAGS/-pipe/}
  CXXFLAGS=${CXXFLAGS/-pipe/}

  # Force this for now, doesn't seem to be picked up via patch from https://bugs.archlinux.org/task/70701
  CFLAGS+=" -Wno-format -Wno-format-security"
  CXXFLAGS+=" -Wno-format -Wno-format-security"

  "$srcdir/gcc/configure" --prefix=/usr \
      --libdir=/usr/lib \
      --libexecdir=/usr/lib \
      --mandir=/usr/share/man \
      --infodir=/usr/share/info \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-languages=c,c++,fortran,lto \
      --enable-shared \
      --enable-threads=posix \
      --enable-libmpx \
      --with-system-zlib \
      --with-isl \
      --enable-__cxa_atexit \
      --disable-libunwind-exceptions \
      --enable-clocale=gnu \
      --disable-libstdcxx-pch \
      --disable-libssp \
      --enable-gnu-unique-object \
      --enable-linker-build-id \
      --enable-lto \
      --enable-plugin \
      --enable-install-libiberty \
      --with-linker-hash-style=gnu \
      --enable-gnu-indirect-function \
      --disable-multilib \
      --disable-werror \
      --enable-checking=release \
      --enable-default-pie \
      --enable-default-ssp \
      --enable-cet=auto \
      --program-suffix=-${_pkgver} \
      --enable-version-specific-runtime-libs

  make

  # make documentation
  make -C $CHOST/libstdc++-v3/doc doc-man-doxygen
}

check() {
  cd gcc-build

  # do not abort on error as some are "expected"
  make -k check || true
  "$srcdir/gcc/contrib/test_summary"
}

package_gcc8-libs() {
  pkgdesc='Runtime libraries shipped by GCC (8.x.x)'
  depends=('glibc>=2.27')
  options+=(!strip)

  cd gcc-build
  make -C $CHOST/libgcc DESTDIR="$pkgdir" install-shared
  mv "$pkgdir"/$_libdir/../lib/* "$pkgdir"/$_libdir
  rmdir "$pkgdir"/$_libdir/../lib
  rm -f "$pkgdir/$_libdir/libgcc_eh.a"

  for lib in libatomic \
             libgfortran \
             libgomp \
             libitm \
             libquadmath \
             libsanitizer/{a,l,ub,t}san \
             libstdc++-v3/src \
             libvtv; do
    make -C $CHOST/$lib DESTDIR="$pkgdir" install-toolexeclibLTLIBRARIES
  done

  make -C $CHOST/libmpx DESTDIR="$pkgdir" install
  rm -f "$pkgdir/${_libdir}/libmpx.spec"

  # Install Runtime Library Exception
  install -Dm644 "$srcdir/gcc/COPYING.RUNTIME" \
    "$pkgdir/usr/share/licenses/gcc8-libs/RUNTIME.LIBRARY.EXCEPTION"
}

package_gcc8() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (8.x.x)"
  depends=("gcc8-libs=$pkgver-$pkgrel" 'binutils>=2.28' libmpc)
  options+=(staticlibs)

  cd gcc-build

  make -C gcc DESTDIR="$pkgdir" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 -t "$pkgdir/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1,gcov,gcov-tool}

  make -C $CHOST/libgcc DESTDIR="$pkgdir" install
  rm -r "$pkgdir"/${_libdir}/../lib

  make -C $CHOST/libstdc++-v3/src DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/include DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/libsupc++ DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/python DESTDIR="$pkgdir" install
  rm "$pkgdir"/${_libdir}/libstdc++.so*

  make DESTDIR="$pkgdir" install-fixincludes
  make -C gcc DESTDIR="$pkgdir" install-mkheaders

  make -C lto-plugin DESTDIR="$pkgdir" install

  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -C $CHOST/libitm DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libquadmath DESTDIR="$pkgdir" install-nodist_libsubincludeHEADERS
  make -C $CHOST/libsanitizer DESTDIR="$pkgdir" install-nodist_{saninclude,toolexeclib}HEADERS
  make -C $CHOST/libsanitizer/asan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/tsan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/lsan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libmpx DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS

  make -C libcpp DESTDIR="$pkgdir" install

  # many packages expect this symlink
  ln -s gcc-${_majorver} "$pkgdir"/usr/bin/cc-${_majorver}

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "$srcdir/c89" "$pkgdir/usr/bin/c89-${_majorver}"
  install -Dm755 "$srcdir/c99" "$pkgdir/usr/bin/c99-${_majorver}"

  # byte-compile python libraries
  python -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"
  python -O -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc8-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"

  # Remove conflicting files
  rm -rf "$pkgdir"/usr/share/locale
}

package_gcc8-fortran() {
  pkgdesc='Fortran front-end for GCC (8.x.x)'
  depends=("gcc8=$pkgver-$pkgrel")

  cd gcc-build
  make -C $CHOST/libgfortran DESTDIR="$pkgdir" install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS}
  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_fincludeHEADERS
  make -C gcc DESTDIR="$pkgdir" fortran.install-common
  install -Dm755 gcc/f951 "$pkgdir/${_libdir}/f951"

  ln -s gfortran-${_majorver} "$pkgdir/usr/bin/f95-${_majorver}"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}
