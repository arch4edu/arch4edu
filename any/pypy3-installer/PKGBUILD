# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=installer
pkgname=pypy3-${_base}
pkgver=1.0.1
pkgrel=1
pkgdesc="A low-level library for installing from a Python wheel distribution"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('6acd541201c5f2b7dc0ae8b8e6d5137ad4eba4faa575e7ddabb239213f03c758f8de3b5888b329b7782397f36610fc877800fb6f41e4f0ee2789111e5e90cf18')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPATH=$(find dist -name 'installer-*.whl') pypy3 -m installer --destdir="$pkgdir" dist/${_base}-*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
