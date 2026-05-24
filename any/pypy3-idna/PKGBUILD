# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=idna
pkgname=pypy3-${_base}
pkgdesc="Internationalized Domain Names in Applications"
pkgver=3.16
pkgrel=1
arch=(any)
url="https://github.com/kjd/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('2d7169a0fdcb09f9401e6f9cfae1ea44d5e6d64d92f8d50033830c9101340e672c199e3c75ce2324129b807610b4310862f5b9f2897da25f462a4e8da9347a71')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
