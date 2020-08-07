# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname='python-sparse'
_pkgname=sparse
pkgver=0.10.0
pkgrel=1
pkgdesc="Sparse multidimensional arrays on top of numpy and scipy"
arch=('any')
url="https://sparse.pydata.org"
license=('BSD-3-clause')
checkdepends=('python-dask' 'python-pytest' 'python-pytest-black' 'python-pytest-cov' 'python-pytest-flake8')
depends=('python' 'python-numpy' 'python-scipy' 'python-numba')
optdepends=()
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/pydata/sparse/archive/$pkgver.tar.gz")
sha256sums=('7831052dc3f0c5f6b0d130167b693a9f851fd3fc711d7eef80867f33c68d7d2e')


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
