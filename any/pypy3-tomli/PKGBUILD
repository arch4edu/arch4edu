# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=tomli
pkgname=pypy3-${_base}
pkgver=2.3.0
pkgrel=1
pkgdesc="A lil' TOML parser"
arch=(any)
url="https://github.com/hukkin/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('bd39f9ef09bf43dc48787541ef96781459f66899fab12f72b24e57ef13a8975e135b6a90b0ed7f44c0c3171a4b3afbe0c8a2a8ffeace4255771a0f331288835e')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
