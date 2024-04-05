# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
pkgname=rocm-gdb
pkgver=6.0.2
pkgrel=2
pkgdesc='ROCm source-level debugger for Linux, based on GDB'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCgdb'
license=('GPL-3.0-or-later')
depends=('glibc' 'gcc-libs' 'rocm-dbgapi' 'bash' 'python' 'guile' 'ncurses' 'expat'
         'xz' 'zlib' 'zstd' 'mpfr' 'gmp' 'libelf' 'readline')
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
        --disable-binutils \
        --disable-gprofng \
        --disable-gprof \
        --enable-tui \
        --enable-64-bit-bfd \
        --enable-targets="amdgcn-amd-amdhsa" \
        --with-system-readline \
        --with-python=/usr/bin/python \
        --with-expat \
        --with-system-zlib \
        --with-lzma \
        --disable-gdbtk \
        --disable-ld \
        --disable-gas \
        --disable-gdbserver \
        --disable-sim

    make
}

package() {
    cd "$_dirname/build"
    make -C gdb DESTDIR="$pkgdir" install
}
