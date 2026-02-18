# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pybind11
pkgname=pypy3-${_base}
pkgver=3.0.2
pkgrel=1
pkgdesc="A lightweight header-only library that exposes C++ types in Python and vice versa"
arch=(any)
url="https://${_base}.readthedocs.org"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(boost cmake eigen pypy3-build pypy3-installer pypy3-scikit-build-core)
source=(https://github.com/${_base::6}/${_base}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('19bee2c76320e25202ee078b5680ff8a7acfb33494dec29dad984ab04de8bcb01340d9fec37c8cc5ac9015dfc367e60312dcd8506e66ce8f0af4c49db562ddef')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
