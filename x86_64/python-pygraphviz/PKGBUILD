# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: PumpkinCheshire <me at pumpkincheshire dot com>
# Contributor: alienzj <alienchuj@gmail.com>

_base=pygraphviz
pkgname=python-${_base}
pkgver=1.11
pkgrel=1
pkgdesc="Python interface to Graphviz graph drawing package"
arch=('i686' 'x86_64')
url="https://${_base}.github.io"
license=('BSD')
depends=(python graphviz)
makedepends=(python-build python-installer python-wheel python-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.zip)
sha512sums=('3914d29fb214e1f7d59c7849e1e63e783902acd262912eccffbf6a67f8cbf6f540b9f2e84c9e7b4f0d90fae27f451a701a3b75a4dcb15b8a81bed463b34e2ef2')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  mv "${pkgdir}/usr/share/doc/${_base}-${pkgver}" "${pkgdir}/usr/share/doc/${pkgname}"
}
