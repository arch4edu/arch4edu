# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=tomli
pkgname=pypy3-${_base}
pkgver=2.2.1
pkgrel=1
pkgdesc="A lil' TOML parser"
arch=(any)
url="https://github.com/hukkin/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('6bd2600b06b9d41f45ae34172380d3ec162d0e25a7602e8e77ee37bbe165674ff17afc39c4d1f87c9cec9bd1f02003ba5ebaa313a60efca64ef5124f77a2c887')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
