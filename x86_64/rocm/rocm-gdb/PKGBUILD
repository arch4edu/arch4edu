# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
pkgname=rocm-gdb
pkgver=5.6.0
pkgrel=1
pkgdesc='ROCm source-level debugger for Linux, based on GDB'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCgdb'
license=('GPL')
depends=('rocm-dbgapi' 'python' 'guile' 'ncurses' 'expat' 'xz' 'zlib' 'mpfr' 'babeltrace')
makedepends=('texinfo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('997ef1883aac2769552bc7082c70b837f4e98b57d24c133cea52b9c92fb0dee1')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

build() {
    export PKG_CONFIG_PATH="/opt/rocm/share/pkgconfig:$PKG_CONFIG_PATH"
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
