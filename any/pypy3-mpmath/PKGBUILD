# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=mpmath
pkgname=pypy3-${_base}
pkgdesc="Python library for arbitrary-precision floating-point arithmetic"
pkgver=1.4.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-gmpy2)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('fe7c4164963915ad7561e4dfb7cba21dee19296b96ca7134cf49ce016502cb299f7a6f49a9d18ce39bebfc90eae2c4a86692cdb03f5bfd04e0ddfb63f91064f1')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
