# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=mpmath
pkgname=pypy3-${_base}
pkgdesc="Python library for arbitrary-precision floating-point arithmetic"
pkgver=1.4.1
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-gmpy2)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('16f431e98a33fa7764336c64794310901eb1a635468045ffe4a202a84a5e7a439cbae0f56bef47acf22f4181d8e0e73def4483728906d49edab709ce6663dc8d')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
