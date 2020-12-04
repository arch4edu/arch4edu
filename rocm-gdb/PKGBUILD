# Maintainer Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocm-gdb
pkgver=3.10.0
pkgrel=1
pkgdesc='ROCm source-level debugger for Linux, based on GDB'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCgdb'
license=('GPL')
depends=('rocm-dbgapi' 'python' 'guile2.0' 'ncurses' 'expat' 'xz' 'zlib' 'mpfr' 'source-highlight' 'babeltrace')
makedepends=('texinfo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('05455cb47dd42404ee8bba047def6a6846a7e877e7a7db8dcffc7100d5ba16f0')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    # From https://git.archlinux.org/svntogit/packages.git/tree/trunk/PKGBUILD?h=packages/gdb
    # hack! - libiberty configure tests for header files using "$CPP $CPPFLAGS"
    sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure
}

build() {
    cd "$_dirname"
    mkdir -p build && cd build
    ../configure \
        --prefix=/opt/rocm \
        --program-prefix=roc \
        --disable-shared \
        --disable-nls \
        --enable-source-highlight \
        --enable-tui \
        --enable-64-bit-bfd \
        --enable-targets="$CHOST,amdgcn-amd-amdhsa" \
        --with-system-readline \
        --with-python=/usr/bin/python \
        --with-guile=guile-2.0 \
        --with-expat \
        --with-system-zlib \
        --with-babeltrace \
        --with-lzma \
        --disable-gdbtk \
        --disable-ld \
        --disable-gas \
        --disable-gdbserver \
        --disable-sim

    make
}

package() {
    DESTDIR="$pkgdir" make -C "$_dirname/build" install
}
