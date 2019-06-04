# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname='python-sparse'
_pkgname=sparse
pkgver=0.7.0
pkgrel=1
pkgdesc="Sparse multidimensional arrays on top of numpy and scipy"
arch=('any')
url="https://sparse.pydata.org"
license=('BSD-3-clause')
checkdepends=('python-pytest' 'python-pytest-cov' 'python-pytest-flake8')
depends=('python' 'python-numpy' 'python-scipy' 'python-numba')
optdepends=()
makedepends=('python-setuptools')
source=("https://github.com/pydata/sparse/archive/$pkgver.tar.gz")
sha256sums=('7f458a24957d53b25d5d61ba7dcb2c0dd6a31fdb41a5319e872923a2449eaaa0')


package(){
  cd "$srcdir/$_pkgname-$pkgver"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

check(){
  cd "$srcdir/$_pkgname-$pkgver"
  py.test
}
# vim:ts=2:sw=2:et:
