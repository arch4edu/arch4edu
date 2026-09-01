# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=build
pkgname=pypy3-${_base}
pkgver=1.6.0
pkgrel=1
pkgdesc="A simple, correct PEP 517 build frontend"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3-packaging pypy3-pyproject-hooks)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('42105517da9e685f64cf65da082251a77a8a82048d15f7ac517dd1d80819c4ed9dacbc2ec92ee9561ae276de03c65afd8bb1c7ae03f03748de09af2d3820bcd0')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
