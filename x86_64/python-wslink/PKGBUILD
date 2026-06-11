# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=wslink
pkgname=python-${_base}
pkgdesc="Python/JavaScript library for communicating over WebSocket"
pkgver=2.5.7
pkgrel=1
arch=(any)
url="https://github.com/kitware/${_base}"
license=(BSD-3-Clause)
depends=(python-aiohttp python-msgpack)
makedepends=(python-build python-installer python-hatchling python-wheel)
optdepends=('python-cryptography: SSL support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('a3df05ef1ec26b9e9750b27dbb597b1616929f35e00114c728c1c8a20e49d6baf3983ddf91b0bb297151d8040f130f1d3f500abc231ca7934173c825adf4388a')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
