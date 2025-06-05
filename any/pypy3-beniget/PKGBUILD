# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=beniget
pkgname=pypy3-${_base}
pkgver=0.4.2.post1
pkgrel=1
pkgdesc="A static analyzer for Python code"
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-gast)
makedepends=(pypy3-setuptools)
source=(https://pypi.io/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('7270d36e2ae98bd984b7f7e90f43c0dbf7b06601370ae71064a8b0a1babe4ca91e78ec8564a6836221c9a331835834e97670f5c7c0f4d40ff22835338b1ef3db')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
