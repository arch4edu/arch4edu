# Maintainer: David (ReyJamonico) < david at rjamo dot dev >
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Sven-Hendrik Haase <svenstaro@gmail.com>
# Contributor: Konstantin Gizdov <arch@kge.pw>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: libtool requires rebuilt with each new gcc version

pkgbase=gcc7
pkgname=(gcc7 gcc7-libs gcc7-fortran)
pkgver=7.5.0
_pkgver=7
_majorver=${pkgver:0:1}
_islver=0.18
pkgrel=4
pkgdesc='The GNU Compiler Collection (7.x.x)'
arch=(x86_64)
license=(GPL LGPL FDL custom)
url='http://gcc.gnu.org'
makedepends=(binutils libmpc doxygen python subversion flex)
options=(!emptydirs !lto)
source=(https://gcc.gnu.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.xz
        https://gcc.gnu.org/pub/gcc/infrastructure/isl-${_islver}.tar.bz2
        bz84080.patch
        libsanitizer.patch)
sha256sums=('b81946e7f01f90528a1f7352ab08cc602b9ccc05d4e44da4bd501c5a189ee661'
            '6b8b0fd7f81d0a957beb3679c81bbb34ccc7568d5682844d8924424a0dadcb1b'
            'bce05807443558db55f0d6b4dae37a678ea1bb3388b541c876fe3d110e3717e7'
            'ee25895428a9dbd3217de109a043c54cb9f51e6a04a260be088a619c0f677e68')

_svnrev=266882
_svnurl=svn://gcc.gnu.org/svn/gcc/branches/gcc-${_majorver}-branch
_libdir=usr/lib/gcc/$CHOST/${pkgver%%+*}

snapshot() {
  svn export -r${_svnrev} ${_svnurl} gcc-r${_svnrev}

  local datestamp basever _pkgver
  basever=$(< gcc-r${_svnrev}/gcc/BASE-VER)
  datestamp=$(< gcc-r${_svnrev}/gcc/DATESTAMP)
  _pkgver=${basever}-${datestamp}

  mv gcc-r${_svnrev} gcc-${_pkgver}
  tar cf - gcc-${_pkgver} | xz > gcc-${_pkgver}.tar.xz
  rm -rf gcc-${_pkgver}
  gpg -b gcc-${_pkgver}.tar.xz
  scp gcc-${_pkgver}.tar.xz{,.sig} sources.archlinux.org:/srv/ftp/other/gcc/

  echo
  echo "pkgver=${_pkgver/-/+}"
}

prepare() {
  [[ ! -d gcc ]] && ln -s gcc-${pkgver/+/-} gcc
  cd gcc

  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=84080
  patch -p0 -i "$srcdir/bz84080.patch"

  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=92154
  patch -Np0 -i "${srcdir}/libsanitizer.patch"

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
  export LD_PRELOAD=/usr/lib/libstdc++.so

  cd gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  # -Werror=format-security causes compilation errors with GCC>10
  # And protection flags leave libgcc unusable
  banned_compile_options=("-pipe" "-Werror=format-security" "-fstack-clash-protection" "-fcf-protection")

  for option in "${banned_compile_options[@]}"
  do
    CFLAGS=${CFLAGS/$option/}
    CXXFLAGS=${CXXFLAGS/$option/}
  done

  "$srcdir/gcc/configure" --prefix=/usr \
      --libdir=/usr/lib \
      --libexecdir=/usr/lib \
      --mandir=/usr/share/man \
      --infodir=/usr/share/info \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-languages=c,c++,fortran,lto \
      --disable-multilib \
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
      --disable-werror \
      --enable-checking=release \
      --enable-default-pie \
      --enable-default-ssp \
      --program-suffix=-${_pkgver} \
      --enable-version-specific-runtime-libs

  make

  # make documentation
  make -C $CHOST/libstdc++-v3/doc doc-man-doxygen
}

package_gcc7-libs() {
  pkgdesc='Runtime libraries shipped by GCC (7.x.x)'
  depends=('glibc>=2.27')
  options+=(!strip)

  export LD_PRELOAD=/usr/lib/libstdc++.so

  cd gcc-build
  make -C $CHOST/libgcc DESTDIR="$pkgdir" install-shared
  rm -f "$pkgdir/$_libdir/libgcc_eh.a"
  mv "$pkgdir"/usr/lib/gcc/$CHOST/lib/libgcc_s.so* "$pkgdir"/$_libdir

  for lib in libatomic \
             libcilkrts \
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
  rm -f "$pkgdir"/$_libdir/libmpx.spec

  # Install Runtime Library Exception
  install -Dm644 "$srcdir/gcc/COPYING.RUNTIME" \
    "$pkgdir/usr/share/licenses/gcc7-libs/RUNTIME.LIBRARY.EXCEPTION"
}

package_gcc7() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (7.x.x)"
  depends=("gcc7-libs=$pkgver-$pkgrel" 'binutils>=2.28' libmpc)
  options+=(staticlibs)

  export LD_PRELOAD=/usr/lib/libstdc++.so

  cd gcc-build

  make -C gcc DESTDIR="$pkgdir" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 -t "$pkgdir/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1}

  make -C $CHOST/libgcc DESTDIR="$pkgdir" install
  rm -rf "$pkgdir"/usr/lib/gcc/$CHOST/lib*

  make -C $CHOST/libstdc++-v3/src DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/include DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/libsupc++ DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/python DESTDIR="$pkgdir" install

  make DESTDIR="$pkgdir" install-libcc1
  mv "$pkgdir"/usr/lib/libcc1.so* "$pkgdir"/${_libdir}
  rm -f "$pkgdir"/${_libdir}/libstdc++.so*

  make DESTDIR="$pkgdir" install-fixincludes
  make -C gcc DESTDIR="$pkgdir" install-mkheaders
  make -C lto-plugin DESTDIR="$pkgdir" install

  make -C $CHOST/libcilkrts DESTDIR="$pkgdir" install-nodist_{toolexeclib,cilkinclude}HEADERS
  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -C $CHOST/libitm DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libquadmath DESTDIR="$pkgdir" install-nodist_libsubincludeHEADERS
  make -C $CHOST/libsanitizer DESTDIR="$pkgdir" install-nodist_{saninclude,toolexeclib}HEADERS
  make -C $CHOST/libsanitizer/asan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libmpx DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS

  make -C libcpp DESTDIR="$pkgdir" install

  # many packages expect this symlink
  ln -s gcc-7 "$pkgdir"/usr/bin/cc-7

  rm -f "$pkgdir"/$_libdir/lib{stdc++,gcc_s}.so

  # byte-compile python libraries
  python -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"
  python -O -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc7-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"

  # Remove conflicting files
  rm -rf "$pkgdir"/usr/share/locale
}

package_gcc7-fortran() {
  pkgdesc="Fortran front-end for GCC (7.x.x)"
  depends=("gcc7=$pkgver-$pkgrel")
  options=('!emptydirs')

  export LD_PRELOAD=/usr/lib/libstdc++.so

  cd gcc-build
  make -C $CHOST/libgfortran DESTDIR=$pkgdir install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS}
  make -C $CHOST/libgomp DESTDIR=$pkgdir install-nodist_fincludeHEADERS
  make -C gcc DESTDIR=$pkgdir fortran.install-common
  install -Dm755 gcc/f951 $pkgdir/${_libdir}/f951

  ln -s gfortran-7 ${pkgdir}/usr/bin/f95-${_pkgver}

  # Install Runtime Library Exception
  install -d ${pkgdir}/usr/share/licenses/$pkgname
  ln -s ../gcc-libs/RUNTIME.LIBRARY.EXCEPTION ${pkgdir}/usr/share/licenses/$pkgname/
}
