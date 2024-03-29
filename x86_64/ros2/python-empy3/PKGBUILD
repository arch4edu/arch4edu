# Maintainer: Zhirui Dai <daizhirui at hotmail dot com>

_pkgname=empy
pkgname=python-empy3
pkgver=3.3.4
pkgrel=1
pkgdesc="Powerful and robust templating system for Python"
arch=('any')
url="http://www.alcyone.com/software/empy/"
license=('LGPL')
depends=('python')
replaces=('python-empy')
provides=('python-empy')
conflicts=('python-empy')
makedepends=('python-setuptools')
source=(https://pypi.python.org/packages/source/e/empy/empy-$pkgver.tar.gz)
sha256sums=('73ac49785b601479df4ea18a7c79bc1304a8a7c34c02b9472cf1206ae88f01b3')

build() {
  cd $_pkgname-$pkgver
  python3 setup.py build
}

package() {
  cd $_pkgname-$pkgver
  python3 setup.py install --root="$pkgdir" --optimize=1
}
