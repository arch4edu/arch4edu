# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname='libsearpc'
epoch=2
pkgver=3.2.0
pkgrel=6
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
sha256sums=('683a78cc6dc66d4db5fd90e3260a23845c6a5ff2510b8f55d2f46b86f9c3f271')

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
