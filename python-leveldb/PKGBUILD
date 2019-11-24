# Maintainer : Daniel Bermond <dbermond@archlinux.org>

pkgname=python-leveldb
_name="${pkgname#python-}"
pkgver=0.20
pkgrel=3
pkgdesc='Python bindings for leveldb database library'
arch=('x86_64')
url='https://pypi.python.org/pypi/leveldb/'
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz"::"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
        "${pkgname}-${pkgver}-python3.8-fix.patch"::'https://patch-diff.githubusercontent.com/raw/rjpower/py-leveldb/pull/11.patch'
        'LICENSE')
sha256sums=('9ffc9b68c8c0e0a996e2409e4a95ef1fbb4dcf0f6040b21b9153cbd57c90e079'
            'ca2e6932b3add24e7116d78b2c975714a4dc781f23ba932f017d640c418b3b42'
            'e1223a5ab4b4631a8f841302c6e407738a6195e68f46cfec25438a75949c8689')

prepare() {
    patch -d "leveldb-${pkgver}" -Np1 -i "${srcdir}/${pkgname}-${pkgver}-python3.8-fix.patch"
}

build() {
    cd "leveldb-${pkgver}"
    python setup.py build
}

check() {
    cd "leveldb-${pkgver}/test"
    
    local _pyver
    _pyver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    
    PYTHONPATH="${srcdir}/leveldb-${pkgver}/build/lib.linux-${CARCH}-${_pyver}" python test.py
}

package() {
    cd "leveldb-${pkgver}"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'

    install -D -m644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
