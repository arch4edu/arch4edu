# Contributor: Francois Boulogne <fboulogne at april dot org>
# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-partd
_pkgname=partd
pkgver=0.3.10
pkgrel=1
pkgdesc="Appendable key-value storage"
arch=('any')
url="http://github.com/dask/partd/"
license=('BSD')
depends=('python' 'python-locket' 'python-toolz')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
optdepends=('python-pyzmq' 'python-numpy' 'python-pandas' 'python-blosc')
source=("https://pypi.python.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('33722a228ebcd1fa6f44b1631bdd4cff056376f89eb826d7d880b35b637bcfba')

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
