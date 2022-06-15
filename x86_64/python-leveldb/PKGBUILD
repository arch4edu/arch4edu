# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=python-leveldb
pkgver=0.201
pkgrel=1
pkgdesc='Python bindings for leveldb database library'
arch=('x86_64')
url='https://pypi.python.org/pypi/leveldb/'
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-nose')
_name="${pkgname#python-}"
source=("${pkgname}-${pkgver}.tar.gz"::"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('1cffe776842917e09f073bd6ea5856c64136aebddbe51bd17ea29913472fecbf')

build() {
    cd "leveldb-${pkgver}"
    python setup.py build
}

check() {
    cd "leveldb-${pkgver}"
    local _pyver
    _pyver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    PYTHONPATH="$(pwd)/build/lib.linux-${CARCH}-${_pyver}" nosetests
}

package() {
    cd "leveldb-${pkgver}"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
