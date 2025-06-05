# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=ply
pkgname=pypy3-${_base}
pkgver=3.11
pkgrel=2
pkgdesc="Implementation of lex and yacc parsing tools"
arch=(any)
url="https://www.dabeaz.com/${_base}"
license=(BSD)
depends=(pypy3)
makedepends=(pypy3-setuptools)
source=(https://pypi.io/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('37e39a4f930874933223be58a3da7f259e155b75135f1edd47069b3b40e5e96af883ebf1c8a1bbd32f914a9e92cfc12e29fec05cf61b518f46c1d37421b20008')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
}
