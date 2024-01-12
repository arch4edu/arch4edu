# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: PumpkinCheshire <me at pumpkincheshire dot com>
# Contributor: alienzj <alienchuj@gmail.com>

_base=pygraphviz
pkgname=python-${_base}
pkgver=1.12
pkgrel=2
pkgdesc="Python interface to Graphviz graph drawing package"
arch=('i686' 'x86_64')
url="https://${_base}.github.io"
license=('custom:BSD-3-clause')
depends=(python graphviz)
makedepends=(python-build python-installer python-wheel python-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('2407fdd7de3b2f7f1d9f9e3e3fe0f19c4faad4a72db33a0b4341a01f98eecd4d240079f2d0ea5cf68a5e10236f11fd84e55fd44518611efde2fab7590e3aae90')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
