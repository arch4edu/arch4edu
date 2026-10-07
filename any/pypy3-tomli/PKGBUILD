# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=tomli
pkgname=pypy3-${_base}
pkgver=2.5.0
pkgrel=1
pkgdesc="A lil' TOML parser"
arch=(any)
url="https://github.com/hukkin/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('f8246d37908e9754295f53499e832804de23213d0b4e73716e6ccf2cc4d119cb3a7e643e6c8cae7eeadf3f31265684b29b06f7b18c721d5dba5763571cb732d5')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
