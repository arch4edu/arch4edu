# Maintainer: Dave Daynard <nardholio@gmail.com>
# Contributor: Sven-Hendrik Haase <svenstaro@archlinux.org>
# Contributor: Torsten Keßler <tpkessler@archlinux.org>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Daniel Kozak <kozzi11@gmail.com>

pkgname=(gcc14 gcc14-libs gcc14-fortran)
pkgver=14.3.1+r516+g5998566829ee
_commit=5998566829eed9f39a316be877a7ce61c7e710ed
pkgrel=1
pkgdesc='The GNU Compiler Collection (14.x.x)'
arch=(x86_64)
license=(GPL-3.0-with-GCC-exception GFDL-1.3-or-later)
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


source=("gcc14::git+https://github.com/gcc-mirror/gcc.git#commit=${_commit}"
        c89 c99
)
sha256sums=('8cb2055c05452126efd50ceb8aa3c6ae31fb70d0df63c0db41217f6378a61d50'
            '7b09ec947f90b98315397af675369a1e3dfc527fa70013062e6e85c4be0275ab'
            '44ea973558842f3f4bd666bdaf6e810fd7b7c7bd36b5cc4c69f93d2cd0124fc7')

pkgver() {
  cd gcc14
  echo "$(cat gcc/BASE-VER)+$(git describe --abbrev=12 --tags | sed 's/[^-]*-[^-]*-//;s/[^-]*-/r&/;s/-/+/g;s/_/./')"
}

prepare() {
  cd gcc14

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64
  sed -i '/lp64=/s/lib64/lib/' gcc/config/aarch64/t-aarch64-linux
  mkdir -p "$srcdir/gcc-build"
}

build() {
  local _confflags=(
      --prefix=/usr
      --libdir=/usr/lib
      --libexecdir=/usr/lib
      --mandir=/usr/share/man
      --infodir=/usr/share/info
      --with-bugurl=https://gitlab.archlinux.org/archlinux/packaging/packages/gcc14/-/issues
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
      --enable-linker-build-id
      --enable-lto
      --disable-multilib
      --enable-plugin
      --enable-shared
      --enable-threads=posix
      --disable-libssp
      --disable-libstdcxx-pch
      --disable-werror
      --program-suffix=-14
      --enable-version-specific-runtime-libs
  )

  cd gcc-build

  # Credits @allanmcrae
  # https://github.com/allanmcrae/toolchain/blob/f18604d70c5933c31b51a320978711e4e6791cf1/gcc/PKGBUILD
  # TODO: properly deal with the build issues resulting from this
  CFLAGS=${CFLAGS/-Werror=format-security/}
  CXXFLAGS=${CXXFLAGS/-Werror=format-security/}

  "$srcdir/gcc14/configure" \
    --enable-languages=c,c++,fortran \
    --enable-bootstrap \
    "${_confflags[@]:?_confflags unset}"

  # see https://bugs.archlinux.org/task/71777 for rationale re *FLAGS handling
  make -O STAGE1_CFLAGS="-O2" \
          BOOT_CFLAGS="$CFLAGS" \
          BOOT_LDFLAGS="$LDFLAGS" \
          LDFLAGS_FOR_TARGET="$LDFLAGS" \
          bootstrap \
          -j$(nproc)

  # make documentation
  make -O -C $CHOST/libstdc++-v3/doc doc-man-doxygen
}

check() {
  cd gcc-build

  # do not abort on error as some are "expected"
  make -O -k check || true
  "$srcdir/gcc14/contrib/test_summary"
}

package_gcc14-libs() {
  pkgdesc='Runtime libraries shipped by GCC (14.x.x)'
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
  install -Dm644 "$srcdir/gcc14/COPYING.RUNTIME" \
    "$pkgdir/usr/share/licenses/gcc14-libs/RUNTIME.LIBRARY.EXCEPTION"

  # remove conflicting files
  rm -rf "${pkgdir}"/usr/share/locale
}

package_gcc14() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (14.x.x)"
  depends=("gcc14-libs" 'binutils>=2.28' libmpc zstd libisl.so)
  options=(!emptydirs staticlibs)

  cd gcc-build

  make -C gcc DESTDIR="$pkgdir" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 -t "$pkgdir/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1,gcov{,-tool}}

  make -C $CHOST/libgcc DESTDIR="$pkgdir" install
  rm -f "${pkgdir}/${_libdir}"/../lib/libgcc_s.so*
  rmdir "${pkgdir}/${_libdir}"/../lib

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
  ln -s gcc-14 "$pkgdir"/usr/bin/cc-14

  # create cc-rs compatible symlinks
  # https://github.com/rust-lang/cc-rs/blob/1.0.73/src/lib.rs#L2578-L2581
  for binary in {c++,g++,gcc,gcc-ar,gcc-nm,gcc-ranlib}; do
    ln -s /usr/bin/${binary} "${pkgdir}"/usr/bin/x86_64-linux-gnu-${binary}-14
  done

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "$srcdir/c89" "$pkgdir/usr/bin/c89-14"
  install -Dm755 "$srcdir/c99" "$pkgdir/usr/bin/c99-14"

  # byte-compile python libraries
  python -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"
  python -O -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc14-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"

  # remove conflicting files
  rm -rf "${pkgdir}"/usr/share/locale
}

package_gcc14-fortran() {
  pkgdesc='Fortran front-end for GCC (14.x.x)'
  depends=("gcc14" libisl.so)

  cd gcc-build
  make -C $CHOST/libgfortran DESTDIR="$pkgdir" install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS,gfor_cHEADERS}
  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_fincludeHEADERS
  make -C gcc DESTDIR="$pkgdir" fortran.install-common
  install -Dm755 gcc/f951 "$pkgdir/${_libdir}/f951"

  ln -s gfortran-14 "$pkgdir/usr/bin/f95-14"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/gcc14-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}
