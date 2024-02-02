# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=wslink
pkgname=python-${_base}
pkgdesc="Python/JavaScript library for communicating over WebSocket"
pkgver=1.12.4
pkgrel=1
arch=(any)
url="https://github.com/kitware/${_base}"
license=('custom:BSD-3-clause')
depends=(python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
optdepends=('python-cryptography: SSL support'
  'ipython: jupyter backend support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('46eee2da69608548d3891fc6be8d581fa01d27fe0f6476a68888723594352ca9fc2493c1f3692e793a55027e5fc6644fa2bb15ce276d5f4ce885766d589b3d7c')

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
