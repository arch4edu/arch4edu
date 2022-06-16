# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname='python-sparse'
_pkgname=sparse
pkgver=0.13.0
pkgrel=1
pkgdesc="Sparse multidimensional arrays on top of numpy and scipy"
arch=('any')
url="https://sparse.pydata.org"
license=('BSD-3-clause')
checkdepends=('python-dask' 'python-pytest' 'python-pytest-black' 'python-pytest-cov' 'python-pytest-flake8' 'python-toolz')
depends=('python-numpy' 'python-scipy' 'python-numba')
optdepends=()
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/pydata/sparse/archive/$pkgver.tar.gz")
sha256sums=('c1f37c2097dfb017789ade963cebd199151b015aa6a30eece2359eb4e3c545e1')

build(){
  cd "$_pkgname-$pkgver"
  python setup.py build
}

package(){
  cd "$_pkgname-$pkgver"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

check(){
  cd "$_pkgname-$pkgver"
  PYTHONPATH=. pytest sparse
}
# vim:ts=2:sw=2:et:
