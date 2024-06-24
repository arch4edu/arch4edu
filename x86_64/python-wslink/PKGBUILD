# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=wslink
pkgname=python-${_base}
pkgdesc="Python/JavaScript library for communicating over WebSocket"
pkgver=2.1.1
pkgrel=1
arch=(any)
url="https://github.com/kitware/${_base}"
license=(BSD-3-Clause)
depends=(python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
optdepends=('python-cryptography: SSL support'
  'ipython: jupyter backend support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('1d8b9cf2f64d90d2737de5e9b9f691246bb661cc4871cb008a970c97c9996630c7c8063479d888025bee76c40699296b12c509a06b72993cb5a1d7029b761cb5')

prepare() {
  sed -i 's/^include/#include/' ${_base}-${pkgver}/python/MANIFEST.in
}

build() {
  cd ${_base}-${pkgver}/python
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}/python
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
