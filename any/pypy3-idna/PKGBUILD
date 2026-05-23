# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=idna
pkgname=pypy3-${_base}
pkgdesc="Internationalized Domain Names in Applications"
pkgver=3.15
pkgrel=1
arch=(any)
url="https://github.com/kjd/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0c99c3a99f1ea391197f4bf52770338fb44746dfbcfdc324e73daa48f85ad718d91ffaba9750a6a9f04dd66fee0469cf1c9dcb5aef6213fc1206acc2657607c0')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
