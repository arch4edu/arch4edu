# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=beniget
pkgname=pypy3-${_base}
pkgver=0.5.0
pkgrel=1
pkgdesc="A static analyzer for Python code"
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-gast)
makedepends=(pypy3-setuptools)
source=(https://pypi.io/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('7094e5c0759d54738aa10923e96e3b20a50dc7736311e36fda757d16eb47838eae8372da53fb794a6871d0f92a38726889665b78b364a430e253b44de795cb6e')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
