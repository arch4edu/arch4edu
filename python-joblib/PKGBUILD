# Maintainer: Francois Boulogne <fboulogne at april dot org>
pkgname=python-joblib
pkgver=0.12.5
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
md5sums=('7687884346aad93aa607c176d0668279')
