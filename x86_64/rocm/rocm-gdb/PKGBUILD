# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
pkgname=rocm-gdb
pkgver=6.0.2
pkgrel=1
pkgdesc='ROCm source-level debugger for Linux, based on GDB'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCgdb'
license=('GPL-3.0-or-later')
depends=('rocm-dbgapi' 'python' 'guile' 'ncurses' 'expat' 'xz' 'zlib' 'mpfr' 'babeltrace')
makedepends=('texinfo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('69b7c3d63435e7d99088980498c68422e52b69244d10a3a62541633e733286e0')
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
