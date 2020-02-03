# Contributor: Francois Boulogne <fboulogne at april dot org>
# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-partd
_pkgname=partd
pkgver=1.1.0
pkgrel=1
pkgdesc="Appendable key-value storage"
arch=('any')
url="http://github.com/dask/partd/"
license=('BSD')
depends=('python' 'python-locket' 'python-toolz')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
optdepends=('python-blosc' 'python-numpy' 'python-pandas' 'python-pyzmq' 'python-snappy')
source=("https://pypi.python.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('6e258bf0810701407ad1410d63d1a15cfd7b773fd9efe555dac6bb82cc8832b0')

check() {
  cd "$srcdir/$_pkgname-$pkgver"
  export PYTHONPATH=build/lib
  py.test
}

build(){
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:ts=2:sw=2:et:
