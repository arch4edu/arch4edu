# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
pkgname=rocm-gdb
pkgver=5.4.1
pkgrel=1
pkgdesc='ROCm source-level debugger for Linux, based on GDB'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCgdb'
license=('GPL')
depends=('rocm-dbgapi' 'python' 'guile' 'ncurses' 'expat' 'xz' 'zlib' 'mpfr' 'babeltrace')
makedepends=('texinfo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "readline8-support.patch::$url/commit/1add37b567a7dee39d99f37b37802034c3fce9c4.patch")
sha256sums=('c3851a7602699388600abadb4773abe688d521a74958eeefec74425cfb48e413'
            '4d69b9160f11dec789ebae840be2ad87a858c4e170a6b6bd11026f6c372c6879')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/readline8-support.patch"
}

build() {
    cd "$_dirname"
    mkdir -p build && cd build
    ../configure \
        --prefix=/opt/rocm \
        --program-prefix=roc \
        --disable-shared \
        --disable-nls \
        --disable-gprofng \
        --enable-tui \
        --enable-64-bit-bfd \
        --enable-targets="$CHOST,amdgcn-amd-amdhsa" \
        --with-system-readline \
        --with-python=/usr/bin/python \
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
