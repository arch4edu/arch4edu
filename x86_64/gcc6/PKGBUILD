# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Sebastiaan Lokhorst <sebastiaanlokhorst@gmail.com>
# Contributor: frankspace
# Contributor: Renan Manola <rmanola@gmail.com>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Allan McRae <allan@archlinux.org>

pkgbase=gcc6
pkgname=('gcc6' 'gcc6-libs' 'gcc6-fortran' 'gcc6-gcj')
pkgver=6.5.0
_ver=${pkgver%%.*}
_islver=0.18
_cloogver=0.18.4
pkgrel=8
pkgdesc="The GNU Compiler Collection (6.x.x)"
arch=(x86_64)
license=(GPL LGPL FDL custom)
url="https://gcc.gnu.org/gcc-6/"
makedepends=(binutils libmpc doxygen subversion java-environment-common zip jdk8-openjdk gtk2 libart-lgpl libxtst zlib java-runtime)
source=("https://gcc.gnu.org/pub/gcc/releases/gcc-${pkgver}/gcc-${pkgver}.tar.xz"
        "https://gcc.gnu.org/pub/gcc/infrastructure/isl-${_islver}.tar.bz2"
        "http://www.bastoul.net/cloog/pages/download/cloog-${_cloogver}.tar.gz"
        libsanitizer.patch
        c89
        c99
)
sha512sums=('ce046f9a50050fd54b870aab764f7db187fe7ea92eb4aaffb7c3689ca623755604e231f2af97ef795f41c406bb80c797dd69957cfdd51dfa2ba60813f72b7eac'
            '85d0b40f4dbf14cb99d17aa07048cdcab2dc3eb527d2fbb1e84c41b2de5f351025370e57448b63b2b8a8cf8a0843a089c3263f9baee1542d5c2e1cb37ed39d94'
            'd35d67b08ffe13c1a010b65bfe4dd02b0ae013d5b489e330dc950bd3514defca8f734bd37781856dcedf0491ff6122c34eecb4b0fe32a22d7e6bdadea98c8c23'
            'e7861f77d54ac9bc12cfc6d3498a9bc284e72f728435c23866ac0763fb93e94e431d819c3def9f5aa03acbafc437141882e7b3746f4574ec6e5eb66b555cebb6'
            'a02da589b23e4a76b5ca3b3e4e2261ef4cf69dadd9460703f14e34090d4e574025a52acef9f54e897679115e2122b0095d9d7eab556024bb0e9c695915951a58'
            'd17176547a1ed2b7aa4743eb66a06308db182a993985a1905b418dfa46b74723631b17fd0d536adfefbdf4900d3b71cdf1e7d663ad379fa11b58b613dccb931c')

_libdir="/usr/lib/gcc/$CHOST/$pkgver"

prepare() {
  [[ ! -d gcc ]] && ln -s gcc-${pkgver/+/-} gcc

  cd gcc
  # Apply patches.
  patch --forward --strip=2 --input="${srcdir}"/libsanitizer.patch

  # Link isl/cloog for in-tree builds
  ln -sf "../isl-${_islver}" isl
  ln -sf "../cloog-${_cloogver}" cloog

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  # Arch uses python version 3 as default python (for gcc6-gcj).
  sed -i '1s+python+python2+' libjava/contrib/aot-compile.in

  mkdir -p "${srcdir}"/gcc-build
}

build() {
  cd gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  export CFLAGS="${CFLAGS/-pipe/} -Wno-error=format-security -Wformat-security"
  export CXXFLAGS="${CXXFLAGS/-pipe/} -Wno-error=format-security -Wformat-security"

  # Newer gcc versions don't support the same flags as the oldest versions, and it seems
  # that xgcc picks up CFLAGS if CFLAGS_FOR_TARGET aren't set (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=25672).
  export CFLAGS_FOR_TARGET="-march=x86-64 -mtune=generic -O2 -pipe -fno-plt -fexceptions -fstack-protector -Wp,-D_FORTIFY_SOURCE=2 -Wno-error=format-security -Wformat-security"
  export CXXFLAGS_FOR_TARGET="-march=x86-64 -mtune=generic -O2 -pipe -fno-plt -fexceptions -fstack-protector -Wp,-D_FORTIFY_SOURCE=2 -Wno-error=format-security -Wformat-security"

  "${srcdir}/gcc/configure" \
    --prefix=/usr \
    --build="${CHOST}" \
    --libdir=/usr/lib \
    --libexecdir=/usr/lib \
    --mandir=/usr/share/man \
    --infodir=/usr/share/info \
    --with-bugurl=https://bugs.archlinux.org/ \
    --enable-languages=c,c++,fortran,lto,java \
    --with-isl \
    --with-linker-hash-style=gnu \
    --with-system-zlib \
    --enable-__cxa_atexit \
    --enable-build-format-warnings \
    --enable-cet=auto \
    --enable-checking=release \
    --enable-clocale=gnu \
    --enable-default-pie \
    --enable-default-ssp \
    --enable-gnu-indirect-function \
    --enable-gnu-unique-object \
    --disable-install-libiberty \
    --enable-linker-build-id \
    --enable-lto \
    --disable-multilib \
    --enable-plugin \
    --enable-shared \
    --enable-threads=posix \
    --disable-libssp \
    --disable-libstdcxx-pch \
    --disable-libunwind-exceptions \
    --disable-werror \
    --enable-java-awt=gtk \
    --with-java-home="$JAVA_HOME" \
    --enable-libgcj-multifile \
    --enable-version-specific-runtime-libs \
    --enable-build-warnings \
    --program-suffix=-${_ver} \
    --disable-nls

  make

  # make documentation
  make -C "${CHOST}"/libstdc++-v3/doc doc-man-doxygen
}

check() {
  cd gcc-build

  make -k check || true
  "${srcdir}/gcc/contrib/test_summary"
}

package_gcc6-libs() {
  pkgdesc="Runtime libraries shipped by GCC (6.x.x)"
  depends=('glibc>=2.25' zlib)
  options+=(!strip)

  cd gcc-build
  make -C "$CHOST"/libgcc DESTDIR="${pkgdir}" install-shared
  rm "${pkgdir}"/"${_libdir}"/libgcc_eh.a
  mv "${pkgdir}"/usr/lib/gcc/"$CHOST"/lib/libgcc_s.so* "${pkgdir}"/"${_libdir}"

  for lib in libatomic \
             libcilkrts \
             libjava \
             libgfortran \
             libgomp \
             libitm \
             libquadmath \
             libsanitizer/{a,l,ub}san \
             libstdc++-v3/src \
             libvtv; do
    make -C "$CHOST/$lib" DESTDIR="${pkgdir}" install-toolexeclibLTLIBRARIES
  done

  make -C "$CHOST"/libsanitizer/tsan DESTDIR="${pkgdir}" install-toolexeclibLTLIBRARIES
  make -C "$CHOST"/libstdc++-v3/po DESTDIR="${pkgdir}" install
  #make -C "$CHOST"/libmpx DESTDIR="${pkgdir}" install
  #rm "${pkgdir}"/"${_libdir}"/libmpx.spec

  for lib in libgomp \
             libitm \
             libquadmath; do
    make -C "$CHOST"/"$lib" DESTDIR="${pkgdir}" install-info
  done

  # Lazy way of dealing with conflicting files...
  rm -rf "${pkgdir}"/usr/share/{info,locale,man}

  # Install Runtime Library Exception
  install -Dm644 "${srcdir}"/gcc-$pkgver/COPYING.RUNTIME \
    "${pkgdir}"/usr/share/licenses/$pkgbase/RUNTIME.LIBRARY.EXCEPTION
}

package_gcc6() {
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (6.x.x)"
  depends=("gcc6-libs=${pkgver}-${pkgrel}" 'binutils>=2.28' libmpc zlib)
  options+=(staticlibs)

  #export LD_PRELOAD=/usr/lib/libstdc++.so

  cd gcc-build

  make -C gcc DESTDIR="${pkgdir}" install-driver install-cpp install-gcc-ar \
    c++.install-common install-headers install-plugin install-lto-wrapper

  for _i in gcov gcov-dump gcov-tool collect2 collect-ld lto1; do
    install -Dm755 "gcc/$_i" "$pkgdir/usr/bin/${_i}-${_ver}"
  done

  make -C "$CHOST"/libgcc DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/lib/gcc/"${CHOST}"/lib*

  make -C "$CHOST"/libstdc++-v3/src DESTDIR="${pkgdir}" install
  make -C "$CHOST"/libstdc++-v3/include DESTDIR="${pkgdir}" install
  make -C "$CHOST"/libstdc++-v3/libsupc++ DESTDIR="${pkgdir}" install
  make -C "$CHOST"/libstdc++-v3/python DESTDIR="${pkgdir}" install

  make DESTDIR="${pkgdir}" install-libcc1
  install -d "$pkgdir"/usr/share/gdb/auto-load/usr/lib
  #mv "${pkgdir}"/${_libdir}/libstdc++.so.6.*-gdb.py \
  #  "${pkgdir}/usr/share/gdb/auto-load/{_libdir}/"
  rm "${pkgdir}"/"${_libdir}"/libstdc++.so*

  make DESTDIR="${pkgdir}" install-fixincludes
  make -C gcc DESTDIR="${pkgdir}" install-mkheaders

  make -C lto-plugin DESTDIR="${pkgdir}" install
  install -dm755 "${pkgdir}"/usr/lib/bfd-plugins/
  ln -s "${_libdir}"/liblto_plugin.so "${pkgdir}"/usr/lib/bfd-plugins/

  make -C "$CHOST"/libcilkrts DESTDIR="${pkgdir}" install-nodist_{cilkinclude,toolexeclib}HEADERS
  make -C "$CHOST"/libgomp DESTDIR="${pkgdir}" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -C "$CHOST"/libitm DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS
  make -C "$CHOST"/libquadmath DESTDIR="${pkgdir}" install-nodist_libsubincludeHEADERS
  make -C "$CHOST"/libsanitizer DESTDIR="${pkgdir}" install-nodist_{saninclude,toolexeclib}HEADERS
  make -C "$CHOST"/libsanitizer/asan DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS
  #make -C "$CHOST"/libmpx DESTDIR="${pkgdir}" install-nodist_toolexeclibHEADERS

  make -C gcc DESTDIR="${pkgdir}" install-man install-info
  rm "${pkgdir}"/usr/share/man/man1/gfortran-${_ver}.1
  rm "${pkgdir}"/usr/share/info/gfortran.info

  make -C libcpp DESTDIR="${pkgdir}" install
  make -C gcc DESTDIR="${pkgdir}" install-po

  # many packages expect this symlink
  ln -s "gcc-${_ver}" "${pkgdir}"/usr/bin/cc-${_ver}

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "${srcdir}/c89" "${pkgdir}/usr/bin/c89-${_ver}"
  install -Dm755 "${srcdir}/c99" "${pkgdir}/usr/bin/c99-${_ver}"

  # Lazy way of dealing with conflicting files...
  rm -rf "${pkgdir}"/usr/share/{info,locale,man}

  # Move potentially conflicting stuff to version specific subdirectory
  mv "${pkgdir}"/usr/lib/bfd-plugins/liblto_plugin.so "${pkgdir}"/usr/lib/bfd-plugins/liblto_plugin-${_ver}.so
  mv "${pkgdir}"/usr/lib/*.so* "${pkgdir}"/"${_libdir}"/
  install -Dm755 gcc/cc1 "${pkgdir}"/"${_libdir}"/cc1
  install -Dm755 gcc/cc1plus "${pkgdir}"/"${_libdir}"/cc1plus
}

package_gcc6-fortran() {
  pkgdesc="Fortran front-end for GCC"
  depends=("gcc6=$pkgver-$pkgrel" zlib libmpc)

  #export LD_PRELOAD=/usr/lib/libstdc++.so

  cd gcc-build
  make -C "$CHOST"/libgfortran DESTDIR="${pkgdir}" install-cafexeclibLTLIBRARIES \
    install-{toolexeclibDATA,nodist_fincludeHEADERS}
  make -C "$CHOST"/libgomp DESTDIR="${pkgdir}" install-nodist_fincludeHEADERS
  make -C gcc DESTDIR="${pkgdir}" fortran.install-common
  install -Dm755 gcc/f951 "${pkgdir}/${_libdir}/f951"

  ln -s gfortran-${_ver} "${pkgdir}"/usr/bin/f95-${_ver}
}

package_gcc6-gcj() {
  pkgdesc="Java front-end for GCC"
  depends=("gcc6=$pkgver-$pkgrel" libmpc libxtst gtk2 java-runtime libsm)
  replaces=('gcc-gcj')

  # Install libjava.
  cd gcc-build
  make -j1 DESTDIR="${pkgdir}" install-target-libjava

  # Install java-common.
  cd gcc
  make -j1 DESTDIR="${pkgdir}" java.install-common java.install-man

  install -m755 jc1 "${pkgdir}"/"${_libdir}"/
  install -m755 jvgenmain "${pkgdir}"/"${_libdir}"/

  # Remove conflicting files.
  rm "${pkgdir}"/usr/lib/gcc/"$CHOST"/lib/libgcc_s.so*
  rm "${pkgdir}"/"${_libdir}"/libg{cj,ij}*.so*
  rm "${pkgdir}"/"${_libdir}"/libgcc_eh.a
  rm "${pkgdir}"/"${_libdir}"/crtbegin.o
  rm "${pkgdir}"/"${_libdir}"/crtbeginS.o
  rm "${pkgdir}"/"${_libdir}"/crtbeginT.o
  rm "${pkgdir}"/"${_libdir}"/crtend.o
  rm "${pkgdir}"/"${_libdir}"/crtendS.o
  rm "${pkgdir}"/"${_libdir}"/crtfastmath.o
  rm "${pkgdir}"/"${_libdir}"/crtprec32.o
  rm "${pkgdir}"/"${_libdir}"/crtprec64.o
  rm "${pkgdir}"/"${_libdir}"/crtprec80.o
  rm "${pkgdir}"/"${_libdir}"/include/unwind.h
  rm "${pkgdir}"/"${_libdir}"/libgcc.a
  rm "${pkgdir}"/"${_libdir}"/libgcov.a

  # Rename two files to not conflict to classpath
  mv "${pkgdir}"/usr/share/info/cp-tools.info "${pkgdir}"/usr/share/info/cp-tools-gcj.info

  linkdir=$(basename "{$pkgdir}"/usr/lib/gcj-${pkgver%.*})
  ln -sf "$linkdir" "${pkgdir}"/usr/lib/gcj-${pkgver%.*}
  ln -sf "libgcj-${pkgver}.jar" "${pkgdir}"/usr/share/java/libgcj-${pkgver%.?}.jar
  ln -sf "libgcj-${pkgver}.jar" "${pkgdir}"/usr/share/java/libgcj.jar
  ln -sf "libgcj-tools-${pkgver}.jar" "${pkgdir}"/usr/share/java/libgcj-tools-${pkgver%.?}.jar
  ln -sf "libgcj-tools-${pkgver}.jar" "${pkgdir}"/usr/share/java/libgcj-tools.jar
}
