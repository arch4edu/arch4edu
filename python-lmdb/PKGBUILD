# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgbase=python-lmdb
pkgname=('python-lmdb' 'python2-lmdb')
pkgver=0.94
pkgrel=2
pkgdesc='Universal Python3 binding for the LMDB Lightning Database'
arch=('i686' 'x86_64')
url='https://github.com/dw/py-lmdb/'
license=('custom')
depends=('python2' 'lmdb')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
source=("https://github.com/dw/py-lmdb/archive/py-lmdb_${pkgver}.tar.gz")
sha256sums=('68685bbbd3ffe93c71f55b57c00d3704a370c70e04b943e47cbe107ad14a049c')

prepare() {
    cp -a "py-lmdb-py-lmdb_${pkgver}" "py-lmdb-py-lmdb_${pkgver}-py2"
}

build() {
    printf '%s\n' '  -> Building for Python3...'
    cd "py-lmdb-py-lmdb_${pkgver}"
    LMDB_FORCE_SYSTEM='1' python setup.py build
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/py-lmdb-py-lmdb_${pkgver}-py2"
    LMDB_FORCE_SYSTEM='1' python2 setup.py build
}

package_python-lmdb() {
    pkgdesc='Universal Python3 binding for the LMDB Lightning Database'
    depends=('python' 'python-cffi' 'lmdb')
    
    cd "py-lmdb-py-lmdb_${pkgver}"
    LMDB_FORCE_SYSTEM='1' python setup.py install --root="$pkgdir" --optimize='1'
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_python2-lmdb() {
    pkgdesc='Universal Python2 binding for the LMDB Lightning Database'
    depends=('python2' 'python2-cffi' 'lmdb')
    
    cd "py-lmdb-py-lmdb_${pkgver}-py2"
    LMDB_FORCE_SYSTEM='1' python2 setup.py install --root="$pkgdir" --optimize='1'
    
    # license
    install -D -m644 'LICENSE' -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
