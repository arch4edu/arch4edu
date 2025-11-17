# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trove-classifiers
pkgname=pypy3-${_base}
pkgdesc="Canonical source for classifiers on PyPI"
pkgver=2025.11.14.15
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-calver)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('1479d733393b7ed8e65105664651121fcf7f221efec7a8269e067f79ffc0459a5a8f0b8e7018969897174013f46f1e5c5e3fc5c556a58319a0be6b1321b8f2f3')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
