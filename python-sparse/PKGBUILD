# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname='python-sparse'
_pkgname=sparse
pkgver=0.9.1
pkgrel=1
pkgdesc="Sparse multidimensional arrays on top of numpy and scipy"
arch=('any')
url="https://sparse.pydata.org"
license=('BSD-3-clause')
checkdepends=('python-pytest' 'python-pytest-cov' 'python-pytest-flake8')
depends=('python' 'python-numpy' 'python-scipy' 'python-numba')
optdepends=()
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/pydata/sparse/archive/$pkgver.tar.gz")
sha256sums=('4f6ebb2348d141e3bf0c578c003475ee8de3e1a2de84cc955c0ad4bf2715d1c6')


package(){
  cd "$srcdir/$_pkgname-$pkgver"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

check(){
  cd "$srcdir/$_pkgname-$pkgver"
  PYTHONPATH=. py.test sparse/tests
}
# vim:ts=2:sw=2:et:
