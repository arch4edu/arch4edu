# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pythran
pkgname=pypy3-${_base}
pkgdesc="Ahead of Time compiler for numeric kernels"
pkgver=0.18.0
pkgrel=1
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-ply pypy3-numpy pypy3-beniget xsimd boost)
makedepends=(pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('70761b08724264ab048d6943b143123d19d81b65d3a5ab9aa023dc7d989bc51b33e17f9bb81a6e8f25f7bde4745f36d1208c8c2bd49f8d27b7a4776611f310a5')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  rm -r "$pkgdir"/opt/pypy3/lib/py*/site-packages/pythran/{boost,xsimd} # Remove bundled boost and xsimd
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
