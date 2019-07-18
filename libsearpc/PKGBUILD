# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=libsearpc
epoch=1
pkgver=3.1
pkgrel=1
pkgdesc="A simple C language RPC framework (including both server side & client side)"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/libsearpc"
license=('Apache')
depends=("glib2>=2.26.0" "jansson>=2.2.1" "python2-gobject2>=2.26.0" 'python2-simplejson')

_pkgver="${pkgver}-latest"
source=("libsearpc-${pkgver}.tar.gz::${url}/archive/v${_pkgver}.tar.gz"
        "libsearpc.pc.patch")
sha256sums=('e440d94dea969dd4d55a4528cb1efac48e559818469c14eb0e91e1d9f9963fbe'
            'aec39a303aaebc0777a22d8c53367f52f619654d63f62b362d75c1c599e632f4')

prepare () {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    patch -p1 -i "${srcdir}"/libsearpc.pc.patch
}

build () {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    ./autogen.sh
    ./configure --prefix=/usr PYTHON=/usr/bin/python2
    make
}

check () {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    make check
}

package () {
    cd "${srcdir}/${pkgname}-${_pkgver}"
    make DESTDIR="${pkgdir}" install
}
