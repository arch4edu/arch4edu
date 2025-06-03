# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=packaging
pkgname=pypy3-${_base}
pkgver=25.0
pkgrel=1
pkgdesc="Core utilities for Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(Apache-2.0 BSD-2-Clause)
depends=(pypy3)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('fb8419f81f0f817440c0b297fc6e963832e219e7a324bf4e0321f1e131a4822f17a19f2eb033a8d4adb622ccb16db59776ec44906a0c0b34f2877b59b9558c18')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
