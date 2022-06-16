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
source=("$pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('685dc994aa770ee1b23f2d5392819c8429f27958771f8dceb2c4fb80210d5915')

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
