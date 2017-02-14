# Maintainer: Daniel Milde <daniel at milde dot cz>
pkgname=python2-leveldb
_pkgname=leveldb
pkgver=0.20
pkgrel=1
pkgdesc="Python bindings for leveldb database library"
url="https://pypi.python.org/pypi/leveldb"
arch=('any')
license=('BSD')
depends=('snappy' 'leveldb' 'gperftools' 'python2')
makedepends=('python2-setuptools')
source=("https://pypi.io/packages/source/l/$_pkgname/$_pkgname-$pkgver.tar.gz")
md5sums=('d27478fe64d243bf2784efe2d0cd1224')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
