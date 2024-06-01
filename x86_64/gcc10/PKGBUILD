# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Jonathon Fernyhough <jonathon+m2x+dev>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Frederik Schwan <freswa at archlinux dot org>
# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Daniel Kozak <kozzi11@gmail.com>

set -u
pkgbase='gcc10'
pkgname=("${pkgbase}"{,-libs,-fortran})
pkgver='10.5.0'
_majorver="${pkgver%%.*}"
_islver='0.24'
pkgrel='2'
pkgdesc='The GNU Compiler Collection (10.x.x)'
arch=('x86_64')
url='https://gcc.gnu.org'
license=('GPL-3.0-or-later' 'LGPL-3.0+' 'GFDL-1.3' 'LicenseRef-custom')
makedepends=('binutils' 'doxygen' 'git' 'libmpc' 'python')
checkdepends=('dejagnu' 'inetutils')
options=('!emptydirs' '!lto' '!buildflags')
source=(
  "https://sourceware.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.xz"{,.sig}
  "https://sourceware.org/pub/gcc/infrastructure/isl-${_islver}.tar.bz2"
  'c89'
  'c99'
)
validpgpkeys=(
  'F3691687D867B81B51CE07D9BBE43771487328A9'  # bpiotrowski@archlinux.org
  '86CFFCA918CF3AF47147588051E8B148A9999C34'  # evangelos@foutrelis.com
  '13975A70E63C361C73AE69EF6EEB81F8981C74C7'  # richard.guenther@gmail.com
  'D3A93CAD751C2AF4F8C7AD516C35B99309B5FA62'  # Jakub Jelinek <jakub@redhat.com>
)
md5sums=('c7d1958570fbd1cd859b015774b9987a'
         'SKIP'
         'dd2f7b78e118c25bd96134a52aae7f4d'
         'd5fd2672deb5f97a2c4bdab486470abe'
         'd99ba9f4bd860e274f17040ee51cd1bf')
b2sums=('9b71761f4015649514677784443886e59733ac3845f7dfaa4343f46327d36c08c403c444b9e492b870ac0b3f2e3568f972b7700a0ef05a497fb4066079b3143b'
        'SKIP'
        '88a178dad5fe9c33be5ec5fe4ac9abc0e075a86cff9184f75cedb7c47de67ce3be273bd0db72286ba0382f4016e9d74855ead798ad7bccb015b853931731828e'
        'a76d19c7830b0a141302890522086fc1548c177611501caac7e66d576e541b64ca3f6e977de715268a9872dfdd6368a011b92e01f7944ec0088f899ac0d2a2a5'
        '02b655b5668f7dea51c3b3e4ff46d5a4aee5a04ed5e26b98a6470f39c2e98ddc0519bffeeedd982c31ef3c171457e4d1beaff32767d1aedd9346837aac4ec3ee')

_CHOST="${CHOST:=}" # https://bbs.archlinux.org/viewtopic.php?pid=2174541
_MAKEFLAGS="${MAKEFLAGS:=}"

_libdir="usr/lib/gcc/${CHOST}/${pkgver%%+*}"

prepare() {
  set -u
  if [ ! -d 'gcc' ]; then
    ln -s "gcc-${pkgver/+/-}" 'gcc'
  fi
  pushd 'gcc' > /dev/null

  # link isl for in-tree build
  ln -s "../isl-${_islver}" 'isl'

  # Do not run fixincludes
  sed -e 's@\./fixinc\.sh@-c true@' -i 'gcc/Makefile.in'

  # Arch Linux installs x86_64 libraries /lib
  sed -e '/m64=/s/lib64/lib/' -i 'gcc/config/i386/t-linux64'

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -e '/ac_cpp=/s/$CPPFLAGS/$CPPFLAGS -O2/' -i 'gcc/configure'

  popd > /dev/null

  rm -rf 'gcc-build'
  mkdir 'gcc-build'

  set +u
}

build() {
  set -u
  export MAKEFLAGS="${_MAKEFLAGS}"
  export CHOST="${_CHOST}"
  cd 'gcc-build'

  if [ ! -s 'Makefile' ]; then
    # The following options are one per line, mostly sorted so they are easy to diff compare to other gcc packages.
    local _conf=(
      --build="${CHOST}"
      --disable-libssp
      --disable-libstdcxx-pch
      --disable-libunwind-exceptions
      --disable-multilib
      --disable-werror
      --enable-__cxa_atexit
      --enable-cet='auto'
      --enable-checking='release'
      --enable-clocale='gnu'
      --enable-default-pie
      --enable-default-ssp
      --enable-gnu-indirect-function
      --enable-gnu-unique-object
      --enable-languages='c,c++,fortran,lto'
      --enable-linker-build-id
      --enable-lto
      --enable-plugin
      --enable-shared
      --enable-threads='posix'
      --enable-version-specific-runtime-libs
      --infodir='/usr/share/info'
      --libdir='/usr/lib'
      --libexecdir='/usr/lib'
      --mandir='/usr/share/man'
      --program-suffix="-${_majorver}"
      --with-bugurl='https://bugs.archlinux.org/'
      --with-isl
      --with-linker-hash-style='gnu'
      --with-pkgversion="Arch Linux ${pkgver}-${pkgrel}"
      --with-system-zlib
      --prefix='/usr'
    )
    ../gcc/configure "${_conf[@]}"
  fi
  LD_PRELOAD='/usr/lib/libstdc++.so' \
  nice make -s

  set +u; msg 'Compile complete'; set -u

  # make documentation
  make -s -j1 -C "${CHOST}/libstdc++-v3/doc" 'doc-man-doxygen'
  set +u
}

check() {
  set -u
  cd 'gcc-build'

  # disable libphobos test to avoid segfaults and other unfunny ways to waste my time
  sed -e '/maybe-check-target-libphobos \\/d' -i 'Makefile'

  # do not abort on error as some are "expected"
  make -O -k check || :
  "${srcdir}/gcc/contrib/test_summary"
  set +u
}

package_gcc10-libs() {
  set -u
  export MAKEFLAGS="${_MAKEFLAGS}"
  export CHOST="${_CHOST}"
  pkgdesc='Runtime libraries shipped by GCC (10.x.x)'
  depends=('glibc>=2.27')
  options=('!emptydirs' '!strip')
  provides=('libgfortran.so' 'libubsan.so' 'libasan.so' 'libtsan.so' 'liblsan.so')

  cd 'gcc-build'
  LD_PRELOAD='/usr/lib/libstdc++.so' \
  make -C "${CHOST}/libgcc" DESTDIR="${pkgdir}" install-shared
  mv "${pkgdir}/${_libdir}"/../lib/* "${pkgdir}/${_libdir}"
  rmdir "${pkgdir}/${_libdir}/../lib"
  rm -f "${pkgdir}/${_libdir}/libgcc_eh.a"

  local _lib
  for _lib in libatomic \
              libgfortran \
              libgomp \
              libitm \
              libquadmath \
              libsanitizer/{a,l,ub,t}san \
              libstdc++-v3/src \
              libvtv; do
    make -C "${CHOST}/${_lib}" DESTDIR="${pkgdir}" install-toolexeclibLTLIBRARIES
  done

  make -C "${CHOST}/libstdc++-v3/po" DESTDIR="${pkgdir}" install

  # Install Runtime Library Exception
  install -Dm644 "${srcdir}/gcc/COPYING.RUNTIME" \
    "${pkgdir}/usr/share/licenses/${pkgname}/RUNTIME.LIBRARY.EXCEPTION"

  # remove conflicting files
  rm -rf "${pkgdir}/usr/share/locale"
  set +u
}

package_gcc10() {
  set -u
  export MAKEFLAGS="${_MAKEFLAGS}"
  export CHOST="${_CHOST}"
  pkgdesc='The GNU Compiler Collection - C and C++ frontends (10.x.x)'
  depends=("${pkgbase}-libs=${pkgver}-${pkgrel}" 'binutils>=2.28' 'libmpc' 'zstd')
  options=('!emptydirs' 'staticlibs')

  cd 'gcc-build'

  make -C 'gcc' DESTDIR="${pkgdir}" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  install -m755 -t "${pkgdir}/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1,gcov{,-tool}}

  make -C "${CHOST}/libgcc" DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}/${_libdir}/../lib"

  make -C "${CHOST}/libstdc++-v3/src" DESTDIR="${pkgdir}" install
  make -C "${CHOST}/libstdc++-v3/include" DESTDIR="${pkgdir}" install
  make -C "${CHOST}/libstdc++-v3/libsupc++" DESTDIR="${pkgdir}" install
  make -C "${CHOST}/libstdc++-v3/python" DESTDIR="${pkgdir}" install
  rm -f "${pkgdir}/${_libdir}"/libstdc++.so*

  make DESTDIR="${pkgdir}" install-fixincludes
  make -C 'gcc' DESTDIR="${pkgdir}" install-mkheaders

  make -C 'lto-plugin' DESTDIR="${pkgdir}" install
  install -dm755 "${pkgdir}/${_libdir}/bfd-plugins/"
  ln -s "/${_libdir}/liblto_plugin.so" \
    "${pkgdir}/${_libdir}/bfd-plugins/"

  make -C "${CHOST}/libgomp" DESTDIR="${pkgdir}" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -C "${CHOST}/libitm" DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS
  make -C "${CHOST}/libquadmath" DESTDIR="${pkgdir}" install-nodist_libsubincludeHEADERS
  make -C "${CHOST}/libsanitizer" DESTDIR="${pkgdir}" install-nodist_{saninclude,toolexeclib}HEADERS
  make -C "${CHOST}/libsanitizer/asan" DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS
  make -C "${CHOST}/libsanitizer/tsan" DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS
  make -C "${CHOST}/libsanitizer/lsan" DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS

  make -C 'libcpp' DESTDIR="${pkgdir}" install
  make -C 'gcc' DESTDIR="${pkgdir}" install-po

  # many packages expect this symlink
  ln -s "gcc-${_majorver}" "${pkgdir}/usr/bin/cc-${_majorver}"

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "${srcdir}/c89" "${pkgdir}/usr/bin/c89-${_majorver}"
  install -Dm755 "${srcdir}/c99" "${pkgdir}/usr/bin/c99-${_majorver}"

  # byte-compile python libraries
  python -m 'compileall' "${pkgdir}/usr/share/gcc-${pkgver%%+*}/"
  python -O -m 'compileall' "${pkgdir}/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "${pkgdir}/usr/share/licenses/${pkgname}/"
  ln -s "/usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION" \
    "${pkgdir}/usr/share/licenses/${pkgname}/"

  # Remove conflicting files
  rm -rf "${pkgdir}/usr/share/locale"
  set +u
}

package_gcc10-fortran() {
  set -u
  export MAKEFLAGS="${_MAKEFLAGS}"
  export CHOST="${_CHOST}"
  pkgdesc='Fortran front-end for GCC (10.x.x)'
  depends=("${pkgbase}=${pkgver}-${pkgrel}")

  cd 'gcc-build'
  make -C "${CHOST}/libgfortran" DESTDIR="${pkgdir}" install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS,gfor_cHEADERS}
  make -C "${CHOST}/libgomp" DESTDIR="${pkgdir}" install-nodist_fincludeHEADERS
  make -C 'gcc' DESTDIR="${pkgdir}" fortran.install-common
  install -Dm755 'gcc/f951' "${pkgdir}/${_libdir}/f951"

  ln -s "gfortran-${_majorver}" "${pkgdir}/usr/bin/f95-${_majorver}"

  # Install Runtime Library Exception
  install -d "${pkgdir}/usr/share/licenses/${pkgname}/"
  ln -s "/usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION" \
    "${pkgdir}/usr/share/licenses/${pkgname}/"
  set +u
}
set +u
