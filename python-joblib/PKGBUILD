# Maintainer: Francois Boulogne <fboulogne at april dot org>
pkgname=python-joblib
pkgver=0.13.2
pkgrel=1
pkgdesc="Set of tools to provide lightweight pipelining in Python."
url="http://pypi.python.org/pypi/joblib"
arch=(any)
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
optdepends=('python-numpy' 'python-lz4')
source=(https://github.com/joblib/joblib/archive/$pkgver.zip)

package() {
    cd $srcdir/joblib-"$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1
}
md5sums=('c29dba54a3334620897b5575a88001aa')
