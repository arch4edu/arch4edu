# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgname=python-leveldb
_name="${pkgname#python-}"
pkgver=0.20
pkgrel=2
pkgdesc='Python bindings for leveldb database library'
arch=('x86_64')
url='https://pypi.python.org/pypi/leveldb/'
license=('BSD')
depends=('python' 'leveldb')
makedepends=('python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz"::"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
        'LICENSE')
sha256sums=('9ffc9b68c8c0e0a996e2409e4a95ef1fbb4dcf0f6040b21b9153cbd57c90e079'
            'e1223a5ab4b4631a8f841302c6e407738a6195e68f46cfec25438a75949c8689')

build() {
    cd "leveldb-${pkgver}"
    python setup.py build
}

check() {
    cd "leveldb-${pkgver}"
    python setup.py test
}

package() {
    cd "leveldb-${pkgver}"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'

    install -D -m644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
