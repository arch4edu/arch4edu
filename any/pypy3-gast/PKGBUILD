# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=gast
pkgname=pypy3-${_base}
pkgdesc="AST that abstracts the underlying Python version"
pkgver=0.6.0
pkgrel=1
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('ddbaba5c38c54956c0c5715a23d0855ececbc1c492d9306c3ac740fef003bd02f2ba004692d46c9bf4aeac98e864cd4418ad58150d98482b663f499c03ec2659')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
