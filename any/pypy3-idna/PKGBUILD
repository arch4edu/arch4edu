# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=idna
pkgname=pypy3-${_base}
pkgdesc="Internationalized Domain Names in Applications"
pkgver=3.19
pkgrel=1
arch=(any)
url="https://github.com/kjd/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('b5c6b9026cc57e0d1e55ec7f541dc41ff5c796dbdb058ad15160a524659289492f3c203106ddf0193f89650fa3cfe889fb237893996e3f0ff1feb29aec7e43db')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
