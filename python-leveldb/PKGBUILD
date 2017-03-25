# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgname=python-leveldb
pkgver=0.20
pkgrel=1
pkgdesc="Python3 bindings for leveldb database library"
arch=('i686' 'x86_64')
url="https://pypi.python.org/pypi/leveldb"
license=('BSD')
depends=('python' 'leveldb')
makedepends=('python-setuptools')
source=("https://pypi.python.org/packages/03/98/1521e7274cfbcc678e9640e242a62cbcd18743f9c5761179da165c940eac/leveldb-${pkgver}.tar.gz")
sha256sums=('9ffc9b68c8c0e0a996e2409e4a95ef1fbb4dcf0f6040b21b9153cbd57c90e079')

build() {
    cd "leveldb-${pkgver}"
    python setup.py build
}

package() {
    cd "leveldb-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize=1
}
