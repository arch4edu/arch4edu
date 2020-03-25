# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname='libsearpc'
epoch=2
pkgver=3.2.0
pkgrel=5
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
source=("libsearpc-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('cd00197fcc40b45b1d5e892b2d08dfa5947f737e0d80f3ef26419334e75b0bff')

prepare () {
    cd "$srcdir/$pkgname-$pkgver"
    sed -i 's|(DESTDIR)@prefix@|@prefix@|' './libsearpc.pc.in'
}

build () {
    cd "$srcdir/$pkgname-$pkgver"
    ./autogen.sh
    ./configure --prefix=/usr PYTHON='/usr/bin/python'
    make
}

check () {
    cd "$srcdir/$pkgname-$pkgver"
    make check
}

package () {
    cd "$srcdir/$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
