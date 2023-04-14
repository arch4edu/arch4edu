# Maintainer: Pellegrino Prevete <pellegrinoprevete at gmail dot com>
# Contributor: elliotwutingfeng
# Contributor: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Jonathon Fernyhough <jonathon+m2x+dev>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Daniel Kozak <kozzi11@gmail.com>

_pkgbase="gcc"
pkgbase="${_pkgbase}11"
pkgname=("${pkgbase}"
         "${pkgbase}-libs"
         "${pkgbase}-fortran")
pkgver=11.3.0
_majorver=${pkgver%%.*}
_islver=0.24
pkgrel=6
pkgdesc='The GNU Compiler Collection (11.x.x)'
arch=(x86_64)
license=(GPL LGPL FDL custom)
url='https://gcc.gnu.org'
makedepends=(
  binutils
  doxygen
  # git
  libmpc
  python
  # libisl.so
)
checkdepends=(dejagnu inetutils)
options=(!emptydirs !lto)
_libdir=usr/lib/gcc/$CHOST/${pkgver%%+*}
_gnu="ftp.gnu.org"
_sourceware="sourceware.org"
_gcc_gnu="${_gnu}/gnu/${_pkgbase}"
_gcc_sourceware="${_sourceware}/pub/${_pkgbase}/releases"
_gcc_host="${_gcc_gnu}"
_gcc_url="https://${_gcc_host}/${_pkgbase}-${pkgver}/${_pkgbase}-${pkgver}.tar.xz"
_isl_gnu="gcc.gnu.org"
_isl_host="${_isl_gnu}"
_isl_url="https://${_isl_host}/pub/gcc/infrastructure/isl-${_islver}.tar.bz2"
source=("${_gcc_url}"{,.sig}
        "${_isl_url}"
        c89 c99
)
validpgpkeys=(F3691687D867B81B51CE07D9BBE43771487328A9  # bpiotrowski@archlinux.org
              86CFFCA918CF3AF47147588051E8B148A9999C34  # evangelos@foutrelis.com
              13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              D3A93CAD751C2AF4F8C7AD516C35B99309B5FA62) # Jakub Jelinek <jakub@redhat.com>
b2sums=('7e562d25446ca4ab9fe8cdb714866f66aba3744d78bf84f31bfb097c1a981e4c7f990cb1e6bcfec5ae6671836a4984e2b70eb8fed81dcef5e244f88da8623469'
        'SKIP'
        '88a178dad5fe9c33be5ec5fe4ac9abc0e075a86cff9184f75cedb7c47de67ce3be273bd0db72286ba0382f4016e9d74855ead798ad7bccb015b853931731828e'
        '2c64090b879d6faea7f20095eff1b9bd6a09fe3b15b3890783d3715171678ab62d32c91af683b878746fb14441dbe09768474417840f96a561443415f76afb63'
        '3cf318835b9833ac7c5d3a6026fff8b4f18b098e18c9649d00e32273688ff06ec3af41f0d0aee9d2261725e0ff08f47a224ccfe5ebb06646aaf318ff8ac9a0d1')

prepare() {
  echo "${_libdir}"
  [[ ! -d gcc ]] && ln -s gcc-${pkgver/+/-} gcc
  cd gcc

  # link isl for in-tree build
  ln -s ../isl-${_islver} isl || true

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" gcc/configure

  mkdir -p "$srcdir/gcc-build"
}

build() {
  local _opts=(
    --prefix=/usr
    --build=$CHOST
    --host=$CHOST
    --target=$CHOST
    --libdir=/usr/lib
    --libexecdir=/usr/lib
    --mandir=/usr/share/man
    --infodir=/usr/share/info
    --with-pkgversion="Arch Linux ${pkgver}-${pkgrel}"
    --with-bugurl=https://bugs.archlinux.org/
    # --enable-bootstrap
    --enable-languages=c,c++,fortran,lto
    --enable-shared
    --enable-threads=posix
    --with-system-zlib
    --with-isl
    --with-linker-hash-style=gnu
    --enable-__cxa_atexit
    --enable-cet=auto
    --enable-checking=release
    --enable-clocale=gnu
    --enable-default-pie
    --enable-default-ssp
    --enable-gnu-indirect-function
    --enable-gnu-unique-object
    --enable-linker-build-id
    --enable-lto
    --enable-plugin
    --disable-libstdcxx-pch
    --enable-install-libiberty
    --disable-libssp
    --disable-libunwind-exceptions
    --disable-werror
    # --with-build-config=bootstrap-lto
    # --enable-link-serialization=1
    --program-suffix=-${_majorver}
    --enable-version-specific-runtime-libs
    --disable-multilib
  )

  cd gcc-build

  export CPPFLAGS=""
  export CFLAGS=""
  export CXXFLAGS=""
  export LDFLAGS=""

  # Credits @allanmcrae
  # https://github.com/allanmcrae/toolchain/blob/f18604d70c5933c31b51a320978711e4e6791cf1/gcc/PKGBUILD
  # TODO: properly deal with the build issues resulting from this
  CFLAGS=${CFLAGS/-Werror=format-security/}
  CXXFLAGS=${CXXFLAGS/-Werror=format-security/}

  local _cflags=(
    -I/usr/include
  )

  local _ldflags=(
    # /${_libdir}/libstdc++.so
  )

  # Work-around `msgfmt: /build/gcc11/src/gcc-build/x86_64-pc-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /usr/lib/libicuuc.so.72)`
  # The trick is borrowed from https://aur.archlinux.org/packages/gcc49
  export LD_PRELOAD="/usr/lib/libstdc++.so"

  # see https://bugs.archlinux.org/task/71777 for rationale re *FLAGS handling

  local _make_opts=(
    STAGE1_CFLAGS='-O2'
    BOOT_CFLAGS="${_cflags[*]}"
    BOOT_LDFLAGS="${_ldflags[*]}"
    LDFLAGS_FOR_TARGET="${_ldflags[*]}"
  )

  # CC="gcc-9" \
  # CXX="g++-9" \
  CPPFLAGS="${_cflags[*]}" \
  CFLAGS="${_cflags[*]}" \
  CXXFLAGS="${_cflags[*]}" \
  LDFLAGS="${_ldflags[*]}" \
  "$srcdir/gcc/configure" ${_opts[*]}

  # CC="gcc-9" \
  # CXX="g++-9" \
  CPPFLAGS="${_cflags[*]}" \
  CFLAGS="${_cflags[*]}" \
  CXXFLAGS="${_cflags[*]}" \
  LDFLAGS="${_ldflags[*]}" \
  LD_PRELOAD="/usr/lib/libstdc++.so" \
  make

  # make documentation
  make -O -C $CHOST/libstdc++-v3/doc doc-man-doxygen
}

check() {
  cd gcc-build

  # disable libphobos test to avoid segfaults and other unfunny ways to waste my time
  sed -i '/maybe-check-target-libphobos \\/d' Makefile

  # do not abort on error as some are "expected"
  make -O -k check || true
  "$srcdir/gcc/contrib/test_summary"
}

package_gcc11-libs() {
  pkgdesc="Runtime libraries shipped by GCC (11.x.x)"
  depends=('glibc>=2.27')
  options=(!emptydirs !strip)
  provides=("${_pkgbase}-libs"
            "libgfortran.so"
            "libubsan.so"
            "libasan.so"
            "libtsan.so"
            "liblsan.so")

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

  # Install Runtime Library Exception
  install -Dm644 "$srcdir/gcc/COPYING.RUNTIME" \
    "$pkgdir/usr/share/licenses/${pkgname}/RUNTIME.LIBRARY.EXCEPTION"

  # remove conflicting files
  rm -rf "${pkgdir}"/usr/share/locale
}

package_gcc11() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (11.x.x)"
  depends=(
    "${pkgbase}-libs=${pkgver}-${pkgrel}"
    'binutils>=2.28'
    # libisl.so
    libmpc
    zstd
  )
  options=(!emptydirs staticlibs)
  provides=("${_pkgbase}")

  cd gcc-build

  make -C gcc DESTDIR="$pkgdir" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 -t "$pkgdir/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1,gcov{,-tool}}

  make -C $CHOST/libgcc DESTDIR="$pkgdir" install
  rm -rf "${pkgdir}/${_libdir}"/../lib

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
  ln -s gcc-${_majorver} "$pkgdir"/usr/bin/cc-${_majorver}

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "$srcdir/c89" "$pkgdir/usr/bin/c89-${_majorver}"
  install -Dm755 "$srcdir/c99" "$pkgdir/usr/bin/c99-${_majorver}"

  # byte-compile python libraries
  python -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"
  python -O -m compileall "$pkgdir/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"

  # Remove conflicting files
  rm -rf "$pkgdir"/usr/share/locale
}

package_gcc11-fortran() {
  pkgdesc='Fortran front-end for GCC (11.x.x)'
  depends=(
    "${pkgbase}=$pkgver-$pkgrel"
    # libisl.so
  )
  provides=("${_pkgbase}-fortran")

  cd gcc-build
  make -C $CHOST/libgfortran DESTDIR="$pkgdir" install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS,gfor_cHEADERS}
  make -C $CHOST/libgomp DESTDIR="$pkgdir" install-nodist_fincludeHEADERS
  make -C gcc DESTDIR="$pkgdir" fortran.install-common
  install -Dm755 gcc/f951 "$pkgdir/${_libdir}/f951"

  ln -s gfortran-${_majorver} "$pkgdir/usr/bin/f95-${_majorver}"

  # Install Runtime Library Exception
  install -d "$pkgdir/usr/share/licenses/$pkgname/"
  ln -s /usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION \
    "$pkgdir/usr/share/licenses/$pkgname/"
}
