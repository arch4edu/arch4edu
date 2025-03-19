# Maintainer: Zhirui Dai <daizhirui at hotmail dot com>

_pkgname=empy
pkgname=python-empy3
pkgver=4.2
pkgrel=1
pkgdesc="Powerful and robust templating system for Python"
arch=('any')
url="http://www.alcyone.com/software/empy/"
license=('BSD-3-Clause')
depends=('python')
replaces=('python-empy')
provides=('python-empy')
conflicts=('python-empy')
makedepends=('python-setuptools')
source=(https://pypi.python.org/packages/source/e/empy/empy-$pkgver.tar.gz)
sha256sums=('86f15e1da9743e79a2e9b2cbacf1a13d0b7fb1835b6254eb253c978b72287f4f')

build() {
  cd $_pkgname-$pkgver
  python3 setup.py build
}

package() {
  cd $_pkgname-$pkgver
  python3 setup.py install --root="$pkgdir" --optimize=1
}
