# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trove-classifiers
pkgname=pypy3-${_base}
pkgdesc="Canonical source for classifiers on PyPI"
pkgver=2026.9.21.13
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-calver)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('033200249edee04c73f11a20ff8a6a0c01c2a47d7aa7232e4e41d4828b8d8fc14e519619f802b5164d8e75345da9b41454b001b92d1cf9a1ce776136863ab505')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
