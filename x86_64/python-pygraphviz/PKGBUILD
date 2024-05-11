# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: PumpkinCheshire <me at pumpkincheshire dot com>
# Contributor: alienzj <alienchuj@gmail.com>

_base=pygraphviz
pkgname=python-${_base}
pkgver=1.13
pkgrel=1
pkgdesc="Python interface to Graphviz graph drawing package"
arch=('i686' 'x86_64')
url="https://${_base}.github.io"
license=('custom:BSD-3-clause')
depends=(python graphviz)
makedepends=(python-build python-installer python-wheel python-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('3159fd9fb1226974c3a6289ebc437eed394021a7fc41669e29879fa6fd5e5cb809c808a4016cfb1afaf30dc10e467e8b0fe5c3b71fb9a1f889efcf5ae6ff3597')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
