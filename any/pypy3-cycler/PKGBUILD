# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=cycler
pkgname=pypy3-${_base}
pkgdesc="Composable style cycles"
pkgver=0.12.1
pkgrel=1
arch=(any)
url="https://github.com/matplotlib/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('f1d264de9c5e63515649aefb5937ef7a85d781c07b1c7c8fe291c969565abb18eb48d6d62f77d278746c60900c93700cbb095d280e09de768aedc2463e60d9a2')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
