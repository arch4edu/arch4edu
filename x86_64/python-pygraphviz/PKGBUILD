# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: PumpkinCheshire <me at pumpkincheshire dot com>
# Contributor: alienzj <alienchuj@gmail.com>

_base=pygraphviz
pkgname=python-${_base}
pkgver=1.10
pkgrel=1
pkgdesc="Python interface to Graphviz graph drawing package"
arch=('i686' 'x86_64')
url="https://${_base}.github.io"
license=('BSD')
depends=(python graphviz)
makedepends=(python-build python-installer python-wheel python-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.zip)
sha512sums=('571c35f7a8013d5f128fcfbbd68372c8660560847afa0648737eae6d305a9283b69dce23a1b1aeb808bd4eac9c9cefa72b1d358fbc47b724a0b70997ea3f6d84')

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
