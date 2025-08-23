# Maintainer: Karl Ludwig Brennan <karlludwigbrennan@outlook.com>
# Contributer: Sven-Hendrik Haase <svenstaro@archlinux.org>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Daniel Kozak <kozzi11@gmail.com>

# toolchain build order: linux-api-headers->glibc->binutils->gcc->glibc->binutils->gcc
# NOTE: libtool requires rebuilt with each new gcc version

pkgname=(gcc12 gcc12-libs gcc12-fortran)
pkgver=12.5.0
_majorver=${pkgver%%.*}
_commit=c17d40bb3778bca5e81595f033df9222b66658eb
pkgrel=2
pkgdesc='The GNU Compiler Collection'
arch=(x86_64)
license=(GPL3 LGPL FDL custom)
url='https://gcc.gnu.org'
makedepends=(
  binutils
  doxygen
  gcc-ada
  gcc-d
  git
  libisl
  libmpc
  python
  zstd
)
checkdepends=(
  dejagnu
  expect
  inetutils
  python-pytest
  tcl
)
options=(!emptydirs !lto)
_libdir=usr/lib/gcc/$CHOST/${pkgver%%+*}
source=(git+https://sourceware.org/git/gcc.git#commit=${_commit}
        c89 c99
        78_all-libsanitizer-Fix-build-with-glibc-2.42.patch
        79_all-sanitizer_common-Remove-reference-to-obsolete-termio.patch
)
validpgpkeys=(F3691687D867B81B51CE07D9BBE43771487328A9  # bpiotrowski@archlinux.org
              86CFFCA918CF3AF47147588051E8B148A9999C34  # evangelos@foutrelis.com
              13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              D3A93CAD751C2AF4F8C7AD516C35B99309B5FA62) # Jakub Jelinek <jakub@redhat.com>
sha256sums=('SKIP'
            'de48736f6e4153f03d0a5d38ceb6c6fdb7f054e8f47ddd6af0a3dbf14f27b931'
            '2513c6d9984dd0a2058557bf00f06d8d5181734e41dcfe07be7ed86f2959622a'
            '17d0dbcdd1772e88853d41575c79e448ddeb8a46ec07b7b15e82c23d75541f8b'
            'b4459b314d33e4b6af1c77c6121dffee262c3ecf5436fc20c67fcab0446e059e')

prepare() {
  [[ ! -d gcc ]] && ln -s gcc-${pkgver/+/-} gcc
  cd gcc

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  # patch for glibc 2.42
  patch -p1 -i "$srcdir/78_all-libsanitizer-Fix-build-with-glibc-2.42.patch"
  patch -p1 -i "$srcdir/79_all-sanitizer_common-Remove-reference-to-obsolete-termio.patch"

  mkdir -p "$srcdir/gcc-build"
}

build() {
  local _confflags=(
      --prefix=/usr
      --libdir=/usr/lib
      --libexecdir=/usr/lib
      --mandir=/usr/share/man
      --infodir=/usr/share/info
      --with-bugurl=https://gitlab.archlinux.org/archlinux/packaging/packages/gcc12/-/issues
      --with-build-config=bootstrap-lto
      --with-linker-hash-style=gnu
      --with-system-zlib
      --enable-__cxa_atexit
      --enable-cet=auto
      --enable-checking=release
      --enable-clocale=gnu
      --enable-default-pie
      --enable-default-ssp
      --enable-gnu-indirect-function
      --enable-gnu-unique-object
      --enable-libstdcxx-backtrace
      --enable-link-serialization=1
      --enable-linker-build-id
      --enable-lto
      --disable-multilib
      --enable-plugin
      --enable-shared
      --enable-threads=posix
      --disable-libssp
      --disable-libstdcxx-pch
      --disable-werror
      --program-suffix=-12
      --enable-version-specific-runtime-libs
  )

  cd gcc-build

  # Credits @allanmcrae
  # https://github.com/allanmcrae/toolchain/blob/f18604d70c5933c31b51a320978711e4e6791cf1/gcc/PKGBUILD
  # TODO: properly deal with the build issues resulting from this
  CFLAGS=${CFLAGS/-Werror=format-security/}
  CXXFLAGS=${CXXFLAGS/-Werror=format-security/}

  "$srcdir/gcc/configure" \
    --enable-languages=c,c++,fortran \
    --enable-bootstrap \
    "${_confflags[@]:?_confflags unset}"

  # see https://bugs.archlinux.org/task/71777 for rationale re *FLAGS handling
  make -O STAGE1_CFLAGS="-O2" \
          BOOT_CFLAGS="$CFLAGS" \
          BOOT_LDFLAGS="$LDFLAGS" \
          LDFLAGS_FOR_TARGET="$LDFLAGS" \
          bootstrap

  # make documentation
  make -O -C $CHOST/libstdc++-v3/doc doc-man-doxygen
}

check() {
  cd gcc-build

  # do not abort on error as some are "expected"
  make -O -k check || true
  "$srcdir/gcc/contrib/test_summary"
}

package_gcc12-libs() {
  pkgdesc='Runtime libraries shipped by GCC (12.x.x)'
  depends=('glibc>=2.27')
  options=(!emptydirs !strip)

  cd gcc-build
  make -C $CHOST/libgcc DESTDIR="$pkgdir" install-shared
  mv "${pkgdir}/${_libdir}"/../lib/* "${pkgdir}/${_libdir}"
  rmdir "${pkgdir}/${_libdir}"/../lib
  rm -f "$pkgdir/$_libdir/libgcc_eh.a"

  for lib in libasan.so \
             libatomic.so \
             libgfortran.so \
             libgomp.so \
             libitm.so \
             liblsan.so \
             libquadmath.so \
             libstdc++.so \
             libtsan.so \
             libubsan.so; do
    ln -s /usr/lib/$lib "$pkgdir/$_libdir/$lib"
  done

  make -C $CHOST/libstdc++-v3/po DESTDIR="$pkgdir" install

  rm -rf "$pkgdir"/$_libdir/include/d/
  rm -f "$pkgdir"/usr/lib/libgphobos.spec

  # Install Runtime Library Exception
  install -Dm644 "$srcdir/gcc/COPYING.RUNTIME" \
    "$pkgdir/usr/share/licenses/gcc12-libs/RUNTIME.LIBRARY.EXCEPTION"

  # remove conflicting files
  rm -rf "${pkgdir}"/usr/share/locale
}

package_gcc12() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (12.x.x)"
  depends=("gcc12-libs" 'binutils>=2.28' libmpc zstd libisl.so)
  options=(!emptydirs staticlibs)

  cd gcc-build

  make -C gcc DESTDIR="$pkgdir" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 -t "$pkgdir/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1,gcov{,-tool}}

  make -C $CHOST/libgcc DESTDIR="$pkgdir" install
  rm -f "$pkgdir"/usr/lib/libgcc_s.so*
  rm -f "$pkgdir"/usr/lib/gcc/x86_64-pc-linux-gnu/lib/libgcc_s.so*

  make -C $CHOST/libstdc++-v3/src DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/include DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/libsupc++ DESTDIR="$pkgdir" install
  make -C $CHOST/libstdc++-v3/python DESTDIR="$pkgdir" install
  rm -f "${pkgdir}/${_libdir}"/libstdc++.so*

  make DESTDIR="$pkgdir" install-fixincludes
  make -C gcc DESTDIR="$pkgdir" install-mkheaders

  make -C lto-plugin DESTDIR="$pkgdir" install
  install -dm755 "$pkgdir"/${_libdir}/bfd-plugins/
  ln -s /${_libdir}/liblto_plugin.so \
    "$pkgdir/${_libdir}/bfd-plugins/"

  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -C $CHOST/libitm DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libquadmath DESTDIR="$pkgdir" install-nodist_libsubincludeHEADERS
  make -C $CHOST/libsanitizer DESTDIR="$pkgdir" install-nodist_{saninclude,toolexeclib}HEADERS
  make -C $CHOST/libsanitizer/asan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/tsan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS
  make -C $CHOST/libsanitizer/lsan DESTDIR="$pkgdir" install-nodist_toolexeclibHEADERS

  make -C libcpp DESTDIR="$pkgdir" install
  make -C gcc DESTDIR="$pkgdir" install-po

  # many packages expect this symlink
  ln -s gcc "$pkgdir"/usr/bin/cc-12

  # create cc-rs compatible symlinks
  # https://github.com/rust-lang/cc-rs/blob/1.0.73/src/lib.rs#L2578-L2581
  for binary in {c++,g++,gcc,gcc-ar,gcc-nm,gcc-ranlib}; do
    ln -s /usr/bin/${binary} "${pkgdir}"/usr/bin/x86_64-linux-gnu-${binary}-12
  done

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "$srcdir/c89" "$pkgdir/usr/bin/c89-12"
  install -Dm755 "$srcdir/c99" "$pkgdir/usr/bin/c99-12"

  # byte-compile python libraries
  python -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"
  python -O -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"

  # remove conflicting files
  rm -rf "${pkgdir}"/usr/share/locale
}

package_gcc12-fortran() {
  pkgdesc='Fortran front-end for GCC (12.x.x)'
  depends=("gcc12" libisl.so)

  cd gcc-build
  make -C $CHOST/libgfortran DESTDIR="$pkgdir" install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS,gfor_cHEADERS}
  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_fincludeHEADERS
  make -C gcc DESTDIR="$pkgdir" fortran.install-common
  install -Dm755 gcc/f951 "$pkgdir/${_libdir}/f951"

  ln -s gfortran-12 "$pkgdir/usr/bin/f95-12"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}
