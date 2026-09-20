# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=idna
pkgname=pypy3-${_base}
pkgdesc="Internationalized Domain Names in Applications"
pkgver=3.20
pkgrel=1
arch=(any)
url="https://github.com/kjd/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('fd3afe8d531a68dde34d18f749765b6e5556aee22c0c2eaf42032ffbb588b833100dd9a7f85eb4e81ddba6d0be051a953d2573f9f98f08ed91c187cd2f8c6613')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
