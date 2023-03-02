# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname='libsearpc'
epoch=2
pkgver=3.3.0
pkgrel=2
pkgdesc="A simple C language RPC framework (including both server side & client side)"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/libsearpc"
license=('Apache')
depends=(
    'glib2'
    'jansson'
    'python-gobject'
    'python-simplejson'
)
_pkgver="${pkgver%.*}-latest"
source=("libsearpc-$_pkgver.tar.gz::$url/archive/v$_pkgver.tar.gz")
sha256sums=('0097b015fc8558f87de24cf7b0ebfd569b968b0c6dac203d789bd74a44404578')

prepare () {
    cd "$srcdir/$pkgname-$_pkgver"
    sed -i 's|(DESTDIR)@prefix@|@prefix@|' './libsearpc.pc.in'
}

build () {
    cd "$srcdir/$pkgname-$_pkgver"
    ./autogen.sh
    ./configure --prefix=/usr PYTHON='/usr/bin/python'
    make
}

check () {
    cd "$srcdir/$pkgname-$_pkgver"
    make check
}

package () {
    cd "$srcdir/$pkgname-$_pkgver"
    make DESTDIR="$pkgdir" install
}
