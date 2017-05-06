# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgbase=python-lmdb
pkgname=('python-lmdb' 'python2-lmdb')
pkgver=0.92
pkgrel=2
arch=('any')
url="https://github.com/dw/py-lmdb/"
license=('custom')
depends=('python2' 'lmdb')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
source=("https://github.com/dw/py-lmdb/archive/py-lmdb_${pkgver}.tar.gz")
sha256sums=('8bed442e5b3dae112613c5f305547575941a7dac2aaa70b2ce68506dd4371a0e')

prepare() {
    cp -a "py-lmdb-py-lmdb_${pkgver}" "py-lmdb-py-lmdb_${pkgver}-py2"
}

build() {
    msg2 "Building for Python3..."
    cd "py-lmdb-py-lmdb_${pkgver}"
    LMDB_FORCE_SYSTEM=1 python setup.py build
    
    msg2 "Building for Python2..."
    cd "${srcdir}/py-lmdb-py-lmdb_${pkgver}-py2"
    LMDB_FORCE_SYSTEM=1 python2 setup.py build
}

package_python-lmdb() {
    pkgdesc="Universal Python3 binding for the LMDB Lightning Database"
    depends=('python' 'python-cffi' 'lmdb')
    
    cd "py-lmdb-py-lmdb_${pkgver}"
    LMDB_FORCE_SYSTEM=1 python setup.py install --root="$pkgdir" --optimize=1
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-lmdb() {
    pkgdesc="Universal Python2 binding for the LMDB Lightning Database"
    depends=('python2' 'python2-cffi' 'lmdb')
    
    cd "py-lmdb-py-lmdb_${pkgver}-py2"
    LMDB_FORCE_SYSTEM=1 python2 setup.py install --root="$pkgdir" --optimize=1
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
