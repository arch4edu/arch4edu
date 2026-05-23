# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=packaging
pkgname=pypy3-${_base}
pkgver=26.2
pkgrel=1
pkgdesc="Core utilities for Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(Apache-2.0 BSD-2-Clause)
depends=(pypy3)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('28a93b2c3ff099eb4ebe82ac09d3c7e7260de37918558d495e2d84a1a8f67603b4b9adb87633ee3d00d953fc0ed50f8b54f573c97ece134fa9b3f5eb636bf05f')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
