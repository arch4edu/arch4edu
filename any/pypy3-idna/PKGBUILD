# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=idna
pkgname=pypy3-${_base}
pkgdesc="Internationalized Domain Names in Applications"
pkgver=3.10
pkgrel=1
arch=(any)
url="https://github.com/kjd/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c3ab2d49ab0b3b96d390a6ca1634d2ea3813655df767868ca72f3d4cb0bf4c6e72830579fe0b43a49dba060cd28a66b041715ff0fd63bb27ed1b6bfa66030625')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
