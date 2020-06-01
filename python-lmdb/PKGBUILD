# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=python-lmdb
pkgver=0.98
pkgrel=1
pkgdesc='Universal Python binding for the LMDB Lightning Database'
arch=('x86_64')
url='https://github.com/jnwatson/py-lmdb/'
license=('custom: OpenLDAP')
depends=('python' 'python-cffi' 'lmdb')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://github.com/jnwatson/py-lmdb/archive/py-lmdb_${pkgver}.tar.gz")
sha256sums=('6e0cd0fb7f53ae95120272bda0117aaef456f80a356808d7ff6c8aa3228fdd17')

build() {
    cd "py-lmdb-py-lmdb_${pkgver}"
    LMDB_FORCE_SYSTEM='1' python setup.py build
}

check() {
    cd "py-lmdb-py-lmdb_${pkgver}"
    local _pyver
    _pyver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    export LMDB_FORCE_SYSTEM='1'
    export PYTHONPATH="$(pwd)/build/lib.linux-${CARCH}-${_pyver}"
    pytest
}

package() {
    cd "py-lmdb-py-lmdb_${pkgver}"
    LMDB_FORCE_SYSTEM='1' python setup.py install --root="$pkgdir" --skip-build --optimize='1'
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
