# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=packaging
pkgname=pypy3-${_base}
pkgver=26.0
pkgrel=1
pkgdesc="Core utilities for Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(Apache-2.0 BSD-2-Clause)
depends=(pypy3)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('9c96b3f70e483af3812a859de217e58e07cc48210cfb3b7e64fbc3118bd7c53c39e9f5f33d13f532a4e0ce4c208bed58c64ed5ea16390371f3480706d72a9011')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
