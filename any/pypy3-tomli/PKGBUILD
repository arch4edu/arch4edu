# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=tomli
pkgname=pypy3-${_base}
pkgver=2.4.1
pkgrel=1
pkgdesc="A lil' TOML parser"
arch=(any)
url="https://github.com/hukkin/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('b7f79c349d5a7309452f940ac630504c52a36761bdcd2b3f451d06172641f59b48721ce15faceb70cd04f995150c9854c6725d6596bebbf06087c7ea95a3d3a4')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
