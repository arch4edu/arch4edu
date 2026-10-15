# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=installer
pkgname=pypy3-${_base}
pkgver=1.1.0
pkgrel=1
pkgdesc="A low-level library for installing from a Python wheel distribution"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('8b237594ff4812c4718c72bf1eb1a0ef1cbdb40f601f9ed1df437733bdfcf2fe14fb9a9769aeda3ec8807d21f9d6aa8e6d418dad86d81102fec43f2eb50dba94')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPATH=$(find dist -name 'installer-*.whl') pypy3 -m installer --destdir="$pkgdir" dist/${_base}-*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
