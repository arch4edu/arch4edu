# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=gmpy2
pkgname=pypy3-${_base}
pkgdesc="Interface to GMP, MPFR, and MPC"
pkgver=2.3.2
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(LGPL-3.0-or-later)
depends=(glibc gmp libmpc mpfr pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${url}/archive/v${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('5d2d3314fc4e58504a31a4be9c4f71a8c9d83511a39bdffc6392b003cffa29a568fea8ce44fe2099cec5a4d6d31ebcec948f6b96c03b59860fb34ffa2da923d1')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
