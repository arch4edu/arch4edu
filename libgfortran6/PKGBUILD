# Maintainer: Hao Zhang <hao [at] hao-zhang [dot] com> 

pkgname=('libgfortran6')
pkgver=6.4.1
_islver=0.17
_cloogver=0.18.4
pkgrel=1
_commit=878763634f0a75699559b3c0b90d466954a6510f
pkgdesc="Fortran runtime libraries shipped by GCC6"
arch=('i686' 'x86_64')
license=('GPL' 'LGPL' 'FDL' 'custom')
url="http://gcc.gnu.org"
makedepends=('binutils>=2.28' 'libmpc' 'git')
source=(git+https://gcc.gnu.org/git/gcc.git#commit=${_commit}
        http://isl.gforge.inria.fr/isl-${_islver}.tar.bz2
        http://www.bastoul.net/cloog/pages/download/cloog-${_cloogver}.tar.gz)
sha1sums=('SKIP'
          '6243384d1b1d4b3043037698485a468a485b111a'
          '8f7568ca1873f8d55bb694c8b9b83f7f4c6c1aa5')

_libdir="/usr/lib/gcc/$CHOST/$pkgver"

prepare() {
  cd ${srcdir}/gcc

  # Link isl/cloog for in-tree builds
  ln -sf ../isl-${_islver} isl
  ln -sf ../cloog-${_cloogver} cloog

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Arch Linux installs x86_64 libraries /lib
  [[ $CARCH == "x86_64" ]] && sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  mkdir ${srcdir}/gcc-build
}

build() {
  cd ${srcdir}/gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  CFLAGS=${CFLAGS/-pipe/}
  CXXFLAGS=${CXXFLAGS/-pipe/}

  ${srcdir}/gcc/configure --prefix=/usr \
      --libdir=/usr/lib \
      --libexecdir=/usr/lib \
      --mandir=/usr/share/man \
      --infodir=/usr/share/info \
      --with-bugurl=https://bugs.archlinux.org/ \
      --enable-languages=fortran \
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
      --with-linker-hash-style=gnu \
      --enable-gnu-indirect-function \
      --disable-multilib \
      --disable-werror \
      --enable-checking=release \
      --enable-default-pie \
      --enable-default-ssp \
      --build="${CHOST}"

  make
}

package()
{
  cd ${srcdir}/gcc-build
  make -C $CHOST/libgfortran DESTDIR=${pkgdir} install-toolexeclibLTLIBRARIES
  rm $pkgdir/usr/lib/*.{so,a}
}
