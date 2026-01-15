# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trove-classifiers
pkgname=pypy3-${_base}
pkgdesc="Canonical source for classifiers on PyPI"
pkgver=2026.1.14.14
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-calver)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('91c9ff8f5ac2794c7603d175f6e7e88e87e2a678066e9709e0ffe869150ef198fa7ce4a93d6181d9b2cfb5385c1eca9169504d9ccc209139fa22c14ce13ebea4')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
