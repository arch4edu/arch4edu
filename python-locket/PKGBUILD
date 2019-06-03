# Contributor: Francois Boulogne <fboulogne at april dot org>
# Maintainer: Francois Boulogne <fboulogne at april dot org>

pkgname=python-locket
_pkgname=locket
pkgver=0.2.0
pkgrel=1
pkgdesc="File-based locks for Python for Linux and Windows"
arch=('any')
url="http://github.com/mwilliamson/locket.py"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=(https://github.com/mwilliamson/locket.py/archive/$pkgver.zip)
sha256sums=('6897c28227c39c2066fe7987d552458d27ddd8578c9c6c2e160d0b0b93092946')

package(){
  cd "$srcdir/$_pkgname.py-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:ts=2:sw=2:et:
