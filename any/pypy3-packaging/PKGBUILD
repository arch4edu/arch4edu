# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=packaging
pkgname=pypy3-${_base}
pkgver=26.3
pkgrel=1
pkgdesc="Core utilities for Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(Apache-2.0 BSD-2-Clause)
depends=(pypy3)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('7559e4f0376c775f57c362394ba276451bee0952012fc461458ee450e86fe89909166bb11c217be100b7909f0958f4ee9df4b51c3019e664186fda06a48d810d')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
