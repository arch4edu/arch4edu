# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

# toolchain build order: linux-api-headers->glibc->binutils->gcc->binutils->glibc
# NOTE: libtool requires rebuilt with each new gcc version
pkgbase=gcc8
pkgname=(gcc8 gcc8-libs gcc8-fortran gcc8-objc gcc8-go)
pkgver=8.3.0
_ver=8
_majorver=${pkgver:0:1}
_islver=0.21
pkgrel=1
pkgdesc='The GNU Compiler Collection'
arch=(x86_64)
license=(GPL LGPL FDL custom)
url='https://gcc.gnu.org'
makedepends=(binutils libmpc doxygen lib32-glibc lib32-gcc-libs python)
#checkdepends=(dejagnu inetutils)
options=(!emptydirs)
source=("https://ftp.gnu.org/gnu/gcc/gcc-$pkgver/gcc-$pkgver.tar.xz"
        "http://isl.gforge.inria.fr/isl-${_islver}.tar.xz"
        "c89" "c99")
sha256sums=('64baadfe6cc0f4947a84cb12d7f0dfaf45bb58b7e92461639596c21e02d97d2c'
            '777058852a3db9500954361e294881214f6ecd4b594c00da5eee974cd6a54960'
            '1ec3372373d0e20b9f32057c0e90ad776086f5d407b388b78b9699a272bf5a3f'
            '30e17222514da5a225272aca3da79bdf3e088656a6a00a7cc6ceab91bea1e032')

_libdir=usr/lib/gcc/$CHOST/${pkgver%%+*}

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

  "$srcdir/gcc/configure" --prefix=/usr \
      --libdir=/usr/lib \
      --libexecdir=/usr/lib \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-languages=c,c++,fortran,go,lto,objc,obj-c++ \
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
      --program-suffix=-${_ver}

  make
}

#check() {
#  cd gcc-build
#
#  # do not abort on error as some are "expected"
#  make -k check || true
#  "$srcdir/gcc/contrib/test_summary"
#}

package_gcc8-libs() {
  pkgdesc='Runtime libraries shipped by GCC (8.x.x)'
  depends=('glibc>=2.27')
  options+=(!strip)

  cd gcc-build
  make -C $CHOST/libgcc DESTDIR="$pkgdir" install-shared
  rm -f "$pkgdir/$_libdir/libgcc_eh.a"
  mv ${pkgdir}/usr/lib/libgcc_s.so* $pkgdir/$_libdir

  for lib in libatomic \
             libgfortran \
             libgo \
             libgomp \
             libitm \
             libquadmath \
             libsanitizer/{a,l,ub,t}san \
             libstdc++-v3/src \
             libvtv; do
    make -C $CHOST/$lib DESTDIR="$pkgdir" install-toolexeclibLTLIBRARIES
  done

  make -C $CHOST/libobjc DESTDIR="$pkgdir" install-libs
  make -C $CHOST/libmpx DESTDIR="$pkgdir" install
  rm -f "$pkgdir/usr/lib/libmpx.spec"

  find ${pkgdir}/usr/lib/ -not -type d -maxdepth 1 -exec mv {} $pkgdir/$_libdir \;

  # remove files provided by lib32-gcc-libs
  rm -rf "$pkgdir"/usr/lib32/

  # Install Runtime Library Exception
  install -Dm644 "$srcdir/gcc/COPYING.RUNTIME" \
    "$pkgdir/usr/share/licenses/${pkgname}/RUNTIME.LIBRARY.EXCEPTION"
}

package_gcc8() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends"
  depends=("gcc8-libs=$pkgver-$pkgrel" 'binutils>=2.28' libmpc)
  options+=(staticlibs)

  cd gcc-build

  make -C gcc DESTDIR="$pkgdir" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  for i in gcov gcov-tool
  do
    install -m755 gcc/$i "$pkgdir/usr/bin/$i-${_ver}"
  done

  for i in cc1 cc1plus collect2 lto1
  do
    install -m755 gcc/$i "$pkgdir/${_libdir}/${i}-${_ver}"
  done

  make -C $CHOST/libgcc DESTDIR="$pkgdir" install
  rm -f "$pkgdir"/usr/lib/libgcc_s.so*

  make -C $CHOST/libstdc++-v3/src DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/include DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/libsupc++ DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/python DESTDIR="$pkgdir" install

  make DESTDIR="$pkgdir" install-libcc1
  install -d "$pkgdir/usr/share/gdb/auto-load/usr/lib"
  #mv "$pkgdir"/usr/lib/libstdc++.so.6.*-gdb.py \
  #  "$pkgdir/usr/share/gdb/auto-load/usr/lib/"
  rm "$pkgdir"/usr/lib/libstdc++.so*

  make DESTDIR="$pkgdir" install-fixincludes
  make -C gcc DESTDIR="$pkgdir" install-mkheaders

  make -C lto-plugin DESTDIR="$pkgdir" install
  install -dm755 "$pkgdir"/usr/lib/bfd-plugins/
  ln -s /${_libdir}/liblto_plugin.so \
    "$pkgdir/usr/lib/bfd-plugins/"

  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -C $CHOST/libitm DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libquadmath DESTDIR="$pkgdir" install-nodist_libsubincludeHEADERS
  make -C $CHOST/libsanitizer DESTDIR="$pkgdir" install-nodist_{saninclude,toolexeclib}HEADERS
  make -C $CHOST/libsanitizer/asan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/tsan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/lsan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libmpx DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS

  find ${pkgdir}/usr/lib/ -not -type d -maxdepth 1 -exec mv {} $pkgdir/$_libdir \;

  make -C libcpp DESTDIR="$pkgdir" install

  # many packages expect this symlink
  ln -s gcc-${_ver} ${pkgdir}/usr/bin/cc-${_ver}

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "$srcdir/c89" "$pkgdir/usr/bin/c89-${_ver}"
  install -Dm755 "$srcdir/c99" "$pkgdir/usr/bin/c99-${_ver}"

  # byte-compile python libraries
  python -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"
  python -O -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc8-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"

  # Lazy way of dealing with conflicting files ...
  rm -rf ${pkgdir}/usr/share/{info,locale,man}

  # Move potentially conflicting stuff to version specific subdirectory
  mv $pkgdir/usr/lib/bfd-plugins/liblto_plugin.so ${pkgdir}/usr/lib/bfd-plugins/liblto_plugin-${_ver}.so
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
  rm -f "$pkgdir/usr/lib/libgfortran.spec"

  ln -s gfortran-${_ver} "$pkgdir/usr/bin/f95-${_ver}"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc8-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}

package_gcc8-objc() {
  pkgdesc='Objective-C front-end for GCC (8.x.x)'
  depends=("gcc8=$pkgver-$pkgrel")

  cd gcc-build
  make DESTDIR="$pkgdir" -C $CHOST/libobjc install-headers
  install -dm755 "$pkgdir/${_libdir}"
  install -m755 gcc/cc1obj{,plus} "$pkgdir/${_libdir}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc8-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}

package_gcc8-go() {
  pkgdesc='Go front-end for GCC (8.x.x)'
  depends=("gcc8=$pkgver-$pkgrel")
  provides=("go=1.10.1")
  conflicts=(go)

  cd gcc-build
  make -C $CHOST/libgo DESTDIR="$pkgdir" install-exec-am
  make DESTDIR="$pkgdir" install-gotools
  make -C gcc DESTDIR="$pkgdir" go.install-common

  rm -f "$pkgdir"/usr/lib/libgo.so*
  install -Dm755 gcc/go1 "$pkgdir/${_libdir}/go1"

  _libdir=usr/lib/go/${pkgver%%+*}/$CHOST
  find ${pkgdir}/usr/lib/ -not -type d -maxdepth 1 -exec mv {} $pkgdir/${_libdir} \;

  # Lazy way of dealing with conflicting files ...
  rm -rf ${pkgdir}/usr/share/{info,locale,man}

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc8-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}
