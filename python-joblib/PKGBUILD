# Maintainer: Francois Boulogne <fboulogne at april dot org>
pkgname=python-joblib
pkgver=0.11
pkgrel=1
pkgdesc="Joblib is a set of tools to provide lightweight pipelining in Python."
url="http://pypi.python.org/pypi/joblib"
arch=(any)
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-nose' 'python-coverage' 'python-numpy' 'python-numpydoc')
source=(https://github.com/joblib/joblib/archive/$pkgver.zip)

# TODO need compiler pkg
#check() {
#    cd $srcdir/joblib-"$pkgver"
#    nosetests3
#}

package() {
    cd $srcdir/joblib-"$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1
}
md5sums=('d8d93e1ded2218933fcc64d5e817d6be')
